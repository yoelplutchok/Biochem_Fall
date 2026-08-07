#!/usr/bin/env python3
"""Pull live Canvas deadlines, flag what changed, warn about what's close.

Rewrites _Planning/DEADLINES.md with current truth and diffs against the last
run to catch due dates that moved, items that appeared, and items that vanished.
Canvas instructors shift dates without announcing it, so the diff is the point --
a snapshot alone goes stale silently.

Two sources, in order of preference:

  1. Canvas API  (canvas_token.conf)  -- exact due times, submission status,
     points. Strongly preferred.
  2. iCal feed   (canvas_feed.conf)   -- fallback. Canvas emits most due dates
     as all-day VALUE=DATE entries, so the 11:59 PM time is LOST, and the feed
     carries no submission status -- everything past its date looks overdue even
     when already turned in.

To use the API, create a token yourself at Canvas -> Account -> Settings ->
"+ New Access Token", then save it (the token string alone) to
_Tools/canvas_token.conf. That file is gitignored. Do not paste it anywhere else.

  python3 _Tools/canvas_deadlines.py              # report + notify
  python3 _Tools/canvas_deadlines.py --quiet      # no macOS notifications
  python3 _Tools/canvas_deadlines.py --days 21    # widen the upcoming window
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

# Paths resolve relative to this file, so the same script works whether it is run
# from the repo by hand or from ~/Library/Application Support by launchd. macOS
# TCC blocks launchd agents from reading ~/Desktop, which is why the scheduled
# copy lives outside the project; MIRROR pushes the report back in when allowed.
ROOT = Path(__file__).resolve().parent.parent
CONF = ROOT / "_Tools" / "canvas_feed.conf"
TOKEN_CONF = ROOT / "_Tools" / "canvas_token.conf"
STATE = ROOT / "_Tools" / ".canvas_state.json"
OUT = ROOT / "_Planning" / "DEADLINES.md"
MIRROR = Path("/Users/yoelplutchok/Desktop/Biochem_Fall/_Planning/DEADLINES.md")
TZ = ZoneInfo("America/New_York")
HOST = "https://touro.instructure.com"

# Course codes in the feed are verbose; shorten for scanning.
SHORT = {
    "Biochemistry and Genetics I": "BIOCHEM",
    "Physiology I": "PHYSIO",
    "Physical Diagnosis I": "PHYS DIAG",
    "Osteopathic Manipulative Medicine 1": "OMM",
    "Clinical Anat & Embryology I": "ANATOMY",
    "Histology I": "HISTO",
    "Professional And Medical Ethics": "ETHICS",
}


def unfold(text):
    """iCal wraps long lines with CRLF + a single space/tab. Undo that first."""
    return re.sub(r"\r?\n[ \t]", "", text)


def unescape(value):
    return (
        value.replace("\\,", ",")
        .replace("\\;", ";")
        .replace("\\n", " ")
        .replace("\\\\", "\\")
        .strip()
    )


def parse_dt(raw):
    raw = raw.split(":")[-1].strip()
    for fmt in ("%Y%m%dT%H%M%SZ", "%Y%m%dT%H%M%S", "%Y%m%d"):
        try:
            dt = datetime.strptime(raw, fmt)
            return dt.replace(tzinfo=timezone.utc) if raw.endswith("Z") else dt.replace(tzinfo=TZ)
        except ValueError:
            continue
    return None


def parse_feed(text):
    events = []
    for block in unfold(text).split("BEGIN:VEVENT")[1:]:
        get = lambda key: (m.group(1) if (m := re.search(rf"^{key}[^:\r\n]*:(.*)$", block, re.M)) else "")
        uid, summary, start = get("UID"), unescape(get("SUMMARY")), parse_dt(get("DTSTART"))
        if not uid or not start:
            continue
        # Canvas formats SUMMARY as "Assignment name [Course Name]".
        course = ""
        if (m := re.search(r"\[([^\]]+)\]\s*$", summary)):
            course = m.group(1).strip()
            summary = summary[: m.start()].strip()
        events.append(
            {
                "uid": uid.strip(),
                "name": summary,
                "course": SHORT.get(course, course),
                "due": start.astimezone(TZ).isoformat(),
                "url": get("URL").strip(),
            }
        )
    events.sort(key=lambda e: e["due"])
    return events


def api_pages(path, token):
    """Follow Canvas Link-header pagination and concatenate the JSON arrays."""
    out, url = [], f"{HOST}{path}"
    while url:
        req = urllib.request.Request(
            url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode("utf-8", "replace")
            page = json.loads(re.sub(r"^while\(1\);", "", body))
            if not isinstance(page, list):
                return out
            out += page
            link = r.headers.get("Link", "") or ""
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
    return out


def fetch_api(token):
    """Exact due times plus submission status -- the reason to prefer this path."""
    events = []
    courses = api_pages("/api/v1/courses?enrollment_state=active&per_page=100", token)
    for c in courses:
        cid, code = c.get("id"), c.get("course_code") or c.get("name") or ""
        if not cid:
            continue
        items = api_pages(
            f"/api/v1/courses/{cid}/assignments?per_page=100&include[]=submission", token
        )
        for a in items:
            if not a.get("due_at"):
                continue
            sub = a.get("submission") or {}
            due = datetime.strptime(a["due_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
            events.append(
                {
                    "uid": f"assignment-{a['id']}",
                    "name": (a.get("name") or "").strip(),
                    "course": SHORT.get(code, code),
                    "due": due.astimezone(TZ).isoformat(),
                    "url": a.get("html_url", ""),
                    "points": a.get("points_possible"),
                    "submitted": bool(sub.get("submitted_at")),
                    "exact_time": True,
                }
            )
    events.sort(key=lambda e: e["due"])
    return events


def notify(title, message):
    """macOS banner. Fails silently -- a missing notifier must not kill the run."""
    try:
        subprocess.run(
            ["osascript", "-e", f'display notification {json.dumps(message)} with title {json.dumps(title)}'],
            check=False,
            capture_output=True,
            timeout=10,
        )
    except Exception:
        pass


def fmt(iso, exact=True):
    """Feed-sourced events are all-day, so printing a time would invent 12:00 AM."""
    dt = datetime.fromisoformat(iso)
    return dt.strftime("%a %b %-d, %-I:%M %p") if exact else dt.strftime("%a %b %-d")


def secret(env_name, path):
    """Env var wins so CI can inject credentials without ever writing them to disk."""
    if os.environ.get(env_name, "").strip():
        return os.environ[env_name].strip()
    if path.exists() and path.read_text().strip():
        return path.read_text().strip()
    return ""


PAGE_CSS = """
*{box-sizing:border-box}
:root{
  --bg:#f6f7f9; --card:#fff; --ink:#14181f; --dim:#5c6673; --line:#e2e6ec;
  --red:#c0392b; --redbg:#fdecea; --amber:#9a6206; --amberbg:#fdf3e0;
  --accent:#1f5fa8;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#12151a; --card:#1a1f27; --ink:#e8ecf2; --dim:#98a3b3; --line:#2a323d;
    --red:#ff8073; --redbg:#3a1e1c; --amber:#ffc266; --amberbg:#3a2f18;
    --accent:#79b0f0;
  }
}
html{-webkit-text-size-adjust:100%}
body{margin:0;padding:1rem;background:var(--bg);color:var(--ink);
  font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:46rem;margin:0 auto}
h1{font-size:1.6rem;margin:.2rem 0 .1rem}
h2{font-size:.82rem;text-transform:uppercase;letter-spacing:.08em;color:var(--dim);
  margin:2rem 0 .6rem;font-weight:600}
.meta{color:var(--dim);font-size:.83rem;margin:0 0 .4rem}
.item{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--line);
  border-radius:9px;padding:.7rem .85rem;margin-bottom:.5rem}
.item.overdue{border-left-color:var(--red);background:var(--redbg)}
.item.soon{border-left-color:var(--amber);background:var(--amberbg)}
.rel{font-weight:700;font-size:1.02rem}
.item.overdue .rel{color:var(--red)}
.item.soon .rel{color:var(--amber)}
.abs{color:var(--dim);font-size:.83rem;margin-left:.5rem}
.what{margin-top:.2rem}
.course{display:inline-block;font-size:.68rem;font-weight:700;letter-spacing:.05em;
  padding:.14rem .42rem;border-radius:4px;background:var(--line);color:var(--dim);
  vertical-align:1px;margin-right:.35rem}
.what a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line)}
.what a:hover{color:var(--accent);border-bottom-color:var(--accent)}
.pts{color:var(--dim);font-size:.8rem;margin-left:.3rem;white-space:nowrap}
.chg{background:var(--card);border:1px solid var(--line);border-radius:9px;
  padding:.6rem .85rem;margin-bottom:.5rem;font-size:.92rem}
.chg b{color:var(--accent)}
.empty{color:var(--dim);font-style:italic;padding:.6rem 0}
.note{color:var(--dim);font-size:.8rem;border-top:1px solid var(--line);
  margin-top:2.2rem;padding-top:.8rem}
.note code{font-size:.94em;background:var(--line);padding:.1em .35em;border-radius:3px}
"""

PAGE_JS = """
// Recompute "in N days" in the browser so a page cached on a phone overnight
// never shows a stale countdown from whenever the build last ran.
for (const el of document.querySelectorAll('[data-due]')) {
  const ms = new Date(el.dataset.due) - new Date();
  const d = Math.round(ms / 86400000), h = Math.round(ms / 3600000);
  el.textContent =
    ms < 0   ? (d === 0 ? 'overdue today' : 'overdue by ' + Math.abs(d) + 'd') :
    h <= 1   ? 'due within the hour' :
    h < 24   ? 'in ' + h + ' hours' :
    d === 1  ? 'tomorrow' : 'in ' + d + ' days';
}
const b = document.getElementById('built');
if (b) {
  const mins = Math.round((new Date() - new Date(b.dataset.at)) / 60000);
  b.textContent = mins < 60 ? mins + ' min ago'
    : mins < 1440 ? Math.round(mins / 60) + ' hr ago'
    : Math.round(mins / 1440) + ' days ago';
}
"""


def card(e, now, kind=""):
    due = datetime.fromisoformat(e["due"])
    exact = e.get("exact_time", False)
    pts = e.get("points")
    name = escape(e["name"])
    link = f'<a href="{escape(e["url"])}">{name}</a>' if e.get("url") else name
    return (
        f'<article class="item {kind}">'
        f'<div><span class="rel" data-due="{due.isoformat()}">…</span>'
        f'<span class="abs">{escape(fmt(e["due"], exact))}</span></div>'
        f'<div class="what"><span class="course">{escape(e["course"] or "—")}</span>'
        f'{link}'
        + (f'<span class="pts">· {pts:g} pts</span>' if pts else "")
        + "</div></article>"
    )


def render_html(now, source, days, overdue, upcoming, later, changes):
    moved, added = changes
    parts = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<meta name="robots" content="noindex,nofollow">',
        # A tab left open on a laptop re-pulls the newest build on its own.
        '<meta http-equiv="refresh" content="1800">',
        "<title>What's due</title>",
        f"<style>{PAGE_CSS}</style>",
        '<div class="wrap">',
        "<h1>What's due</h1>",
        f'<p class="meta">Pulled straight from Canvas '
        f'({"API" if source == "api" else "calendar feed"}) · updated '
        f'<span id="built" data-at="{now.isoformat()}">just now</span> · '
        f'{now:%a %b %-d, %-I:%M %p} ET</p>',
    ]

    if moved or added:
        parts.append("<h2>Changed since the last check</h2>")
        for before, after in moved:
            parts.append(
                f'<div class="chg"><b>Moved</b> · {escape(after["course"])} — '
                f'{escape(after["name"])}<br>{escape(fmt(before["due"], before.get("exact_time", False)))}'
                f' → <b>{escape(fmt(after["due"], after.get("exact_time", False)))}</b></div>'
            )
        for e in added:
            parts.append(
                f'<div class="chg"><b>New</b> · {escape(e["course"])} — {escape(e["name"])}'
                f' — due {escape(fmt(e["due"], e.get("exact_time", False)))}</div>'
            )

    if overdue:
        parts.append(f"<h2>Past due ({len(overdue)})</h2>")
        parts += [card(e, now, "overdue") for e in overdue]

    parts.append(f"<h2>Next {days} days</h2>")
    if upcoming:
        for e in upcoming:
            close = datetime.fromisoformat(e["due"]) - now <= timedelta(days=2)
            parts.append(card(e, now, "soon" if close else ""))
    else:
        parts.append('<p class="empty">Nothing due in the next '
                     f'{days} days.</p>')

    if later:
        parts.append(f"<h2>Rest of the semester ({len(later)})</h2>")
        parts += [card(e, now) for e in later]

    parts.append('<p class="note">')
    if source != "api":
        parts.append(
            "Built from the Canvas <b>calendar feed</b>, which publishes most "
            "assignments as all-day entries — so dates are exact but "
            "<b>times are not shown</b> (Canvas due times are usually 11:59 PM), "
            "and work already turned in is <b>not</b> filtered out. Adding a Canvas "
            "API token fixes both. "
        )
    else:
        parts.append("Exact due times, and anything already submitted is filtered out. ")
    parts.append(
        "Generated by <code>_Tools/canvas_deadlines.py</code> from live Canvas data — "
        "never from a saved copy. Canvas itself is the final word.</p>"
    )
    parts.append(f"</div><script>{PAGE_JS}</script>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=14, help="upcoming window (default 14)")
    ap.add_argument("--quiet", action="store_true", help="skip macOS notifications")
    ap.add_argument(
        "--lead",
        type=int,
        nargs="+",
        default=[3, 1],
        metavar="N",
        help="days before due to remind, fires once each (default: 3 1)",
    )
    ap.add_argument("--html", metavar="PATH", help="also write a standalone web page here")
    ap.add_argument("--state", metavar="PATH", help=f"state file (default {STATE})")
    ap.add_argument("--no-md", action="store_true", help="skip the markdown report")
    args = ap.parse_args()

    state_path = Path(args.state) if args.state else STATE

    source = None
    events = []
    token = secret("CANVAS_TOKEN", TOKEN_CONF)
    if token:
        try:
            events = fetch_api(token)
            source = "api"
        except Exception as exc:
            print(f"API path failed ({exc}); falling back to the iCal feed.\n", file=sys.stderr)

    if not events:
        url = secret("CANVAS_FEED", CONF)
        if not url:
            sys.exit(
                f"No Canvas credential. Set CANVAS_TOKEN or CANVAS_FEED in the "
                f"environment, or put the feed URL in {CONF}."
            )
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                feed = r.read().decode("utf-8", "replace")
        except Exception as exc:
            sys.exit(f"Could not reach the Canvas feed: {exc}")
        events = parse_feed(feed)
        source = "feed"

    if not events:
        sys.exit("No events returned -- the feed URL or token may have been reset in Canvas.")

    # State holds both the last snapshot and which lead-time reminders have already
    # fired, so running twice a day doesn't re-announce the same item every run.
    old, notified = {}, {}
    if state_path.exists():
        try:
            raw = json.loads(state_path.read_text())
            if isinstance(raw, list):  # pre-reminder format
                old = {e["uid"]: e for e in raw}
            else:
                old = {e["uid"]: e for e in raw.get("events", [])}
                notified = raw.get("notified", {})
        except Exception:
            old, notified = {}, {}

    # With no prior state every item looks new. Announcing 32 "NEW" assignments on
    # a first run (or on a fresh CI checkout) is noise, so hold the diff until
    # there is something real to compare against.
    first_run = not old
    new = {e["uid"]: e for e in events}
    added = [] if first_run else [e for u, e in new.items() if u not in old]
    removed = [] if first_run else [e for u, e in old.items() if u not in new]
    moved = [] if first_run else [
        (old[u], e) for u, e in new.items()
        if u in old and old[u]["due"] != e["due"]
    ]

    now = datetime.now(TZ)
    horizon = now + timedelta(days=args.days)
    # Only the API knows what's been turned in. On the feed path `submitted` is
    # absent everywhere, so past-due items stay listed even once handed in.
    done = lambda e: e.get("submitted", False)
    upcoming = [
        e for e in events
        if now <= datetime.fromisoformat(e["due"]) <= horizon and not done(e)
    ]
    overdue = [
        e for e in events if datetime.fromisoformat(e["due"]) < now and not done(e)
    ]
    later = [
        e for e in events
        if datetime.fromisoformat(e["due"]) > horizon and not done(e)
    ]

    # ---- console report ----
    print(f"Canvas deadlines as of {now:%a %b %d %Y, %-I:%M %p}")
    if source == "api":
        print("source: Canvas API (exact times, submitted items filtered out)\n")
    else:
        print(
            "source: iCal feed -- times are DATE-ONLY (Canvas drops the 11:59 PM)\n"
            "        and submitted work cannot be filtered. Add a token for accuracy;\n"
            "        see the header of this script.\n"
        )

    if moved or added or removed:
        print("CHANGED SINCE LAST CHECK")
        for before, after in moved:
            print(f"  ~ MOVED   {after['course']} | {after['name']}")
            print(f"            {fmt(before['due'])}  ->  {fmt(after['due'])}")
        for e in added:
            print(f"  + NEW     {fmt(e['due'])} | {e['course']} | {e['name']}")
        for e in removed:
            print(f"  - GONE    {e['course']} | {e['name']}")
        print()
    elif old:
        print("No changes since last check.\n")

    if overdue:
        print(f"PAST DUE ({len(overdue)})")
        for e in overdue[-5:]:
            print(f"  ! {fmt(e['due'])} | {e['course']} | {e['name']}")
        print()

    print(f"NEXT {args.days} DAYS ({len(upcoming)})")
    for e in upcoming:
        days = (datetime.fromisoformat(e["due"]) - now).days
        flag = "<<" if days <= 2 else "  "
        print(f"  {flag} {fmt(e['due'])} | in {days}d | {e['course']} | {e['name']}")
    if not upcoming:
        print("  nothing due")

    # ---- notifications ----
    if not args.quiet:
        if moved:
            b, a = moved[0]
            extra = f" (+{len(moved)-1} more)" if len(moved) > 1 else ""
            notify("Canvas due date CHANGED", f"{a['name'][:60]} moved to {fmt(a['due'])}{extra}")
        if added:
            notify("New Canvas assignment", f"{added[0]['name'][:60]} due {fmt(added[0]['due'])}")
        # Fire once per (item, lead threshold). An item crossing 3 days notifies at
        # the 3-day mark and again at 1 day, but never twice for the same threshold.
        for e in upcoming:
            left = datetime.fromisoformat(e["due"]) - now
            for lead in sorted(args.lead):
                key = f"{e['uid']}:{lead}"
                if left <= timedelta(days=lead) and key not in notified:
                    when = "tomorrow" if lead == 1 else f"in {lead} days"
                    notify(
                        f"Due {when}: {e['course']}",
                        f"{e['name'][:70]} — {fmt(e['due'])}",
                    )
                    notified[key] = now.isoformat()

        # Drop reminder keys for items that are gone or already past, so the file
        # doesn't grow without bound across a semester.
        live = {
            f"{e['uid']}:{l}"
            for e in events
            for l in args.lead
            if datetime.fromisoformat(e["due"]) >= now
        }
        notified = {k: v for k, v in notified.items() if k in live}

    # ---- write the standalone page ----
    if args.html:
        page = Path(args.html)
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(render_html(now, source, args.days, overdue, upcoming, later,
                                    (moved, added)))
        print(f"Wrote {page}")

    # ---- write the always-current file ----
    if args.no_md:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps({"events": events, "notified": notified}, indent=1))
        return

    OUT.parent.mkdir(parents=True, exist_ok=True)
    md = [
        "# Canvas Deadlines (live)",
        "",
        f"Auto-generated by `_Tools/canvas_deadlines.py` — last refreshed "
        f"**{now:%a %b %d %Y, %-I:%M %p}** ET.",
        "Do not hand-edit; rerun the script instead.",
        "",
    ]
    if moved or added:
        md += ["## Changed since last check", ""]
        for before, after in moved:
            md.append(f"- **MOVED** {after['course']} — {after['name']}: "
                      f"{fmt(before['due'])} → **{fmt(after['due'])}**")
        for e in added:
            md.append(f"- **NEW** {e['course']} — {e['name']} — due {fmt(e['due'])}")
        md.append("")
    if overdue:
        md += ["## Past due", "", "| Due | Course | Item |", "|---|---|---|"]
        md += [f"| {fmt(e['due'])} | {e['course']} | {e['name']} |" for e in overdue]
        md.append("")
    md += [f"## Upcoming — next {args.days} days", "", "| Due | In | Course | Item |", "|---|---|---|---|"]
    md += [
        f"| {fmt(e['due'])} | {(datetime.fromisoformat(e['due']) - now).days}d | {e['course']} | {e['name']} |"
        for e in upcoming
    ] or ["| — | — | — | nothing due |"]
    md += ["", "## Everything remaining", "", "| Due | Course | Item |", "|---|---|---|"]
    md += [
        f"| {fmt(e['due'])} | {e['course']} | {e['name']} |"
        for e in events
        if datetime.fromisoformat(e["due"]) >= now and not done(e)
    ]
    if source != "api":
        md += [
            "",
            "> Generated from the iCal feed: due **times** are date-only (Canvas drops",
            "> the 11:59 PM), and submitted work is not filtered out. Add a Canvas API",
            "> token to `_Tools/canvas_token.conf` for exact times and accurate status.",
        ]
    text = "\n".join(md) + "\n"
    OUT.write_text(text)
    print(f"\nWrote {OUT} ({len(events)} events tracked, source: {source})")

    # Best-effort copy into the Desktop project. Blocked for launchd runs under
    # TCC, which is expected and must not fail the run.
    if sys.platform == "darwin" and MIRROR.resolve() != OUT.resolve():
        try:
            MIRROR.parent.mkdir(parents=True, exist_ok=True)
            MIRROR.write_text(text)
            print(f"Mirrored to {MIRROR}")
        except (PermissionError, OSError):
            print("(project mirror skipped -- macOS blocks background access to ~/Desktop)")

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps({"events": events, "notified": notified}, indent=1))


if __name__ == "__main__":
    main()
