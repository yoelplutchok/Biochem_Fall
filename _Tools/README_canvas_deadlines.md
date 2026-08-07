# Canvas deadline tracker

Keeps a live view of every Canvas due date and warns you before things land.
Set up 2026-08-07.

## The page

**https://yoelplutchok.github.io/Biochem_Fall/deadlines.html**

Rebuilt from Canvas three times a day by a GitHub Action, so it is current
whether or not this laptop is open. Also linked from the site's front page.
Bookmark it on your phone — add to Home Screen and it behaves like an app.

Everything on it is fetched from Canvas at build time. It never reads
`_Planning/ALL_CANVAS_DEADLINES.md` or any other saved copy; those are frozen
snapshots and will disagree with reality as instructors move dates.

`.github/workflows/deadlines.yml` — 7 AM, 1 PM and 7 PM Eastern, plus a
**Run workflow** button on the Actions tab for an instant refresh. Three runs a
day because GitHub delays or occasionally skips scheduled jobs under load.

```bash
gh workflow run deadlines.yml          # refresh now
gh run list --workflow=deadlines.yml   # did it work
```

The Canvas credential lives in **GitHub repo secrets**, never in the repo:
`CANVAS_FEED` is set, `CANVAS_TOKEN` is not (see *Accuracy* below). Actions
masks both in logs. To rotate: `gh secret set CANVAS_FEED < canvas_feed.conf`.

Two things to know. **This repo is public, so the page is public** — anyone with
the link can read your schedule and what is past due. It carries a `noindex` tag
so search engines skip it, but that is obscurity, not privacy. And GitHub
disables scheduled workflows in repositories that sit untouched for 60 days; you
commit coursework often enough that this should not bite, but if the page ever
goes stale, check that first.

## Running it by hand

```bash
python3 ~/Library/Application\ Support/CanvasDeadlines/_Tools/canvas_deadlines.py
python3 _Tools/canvas_deadlines.py --days 30     # repo copy, wider window
python3 _Tools/canvas_deadlines.py --quiet       # no macOS banners
```

## Where things live, and why

The scheduled job runs a copy in
`~/Library/Application Support/CanvasDeadlines/`, **not** from this repo.
macOS TCC blocks launchd agents from reading `~/Desktop`, so a job pointed at
the project fails with `Operation not permitted`. The script tries to mirror
its report back into `_Planning/DEADLINES.md` and skips silently when the OS
refuses. Read the report at:

```
~/Library/Application Support/CanvasDeadlines/_Planning/DEADLINES.md
```

If you'd rather it write straight into the project, grant Full Disk Access to
`/usr/bin/python3` in System Settings → Privacy & Security. That is a broad
permission; the mirror-and-skip arrangement avoids needing it.

**After editing the script in this repo, copy it across or the schedule keeps
running the old one:**

```bash
cp _Tools/canvas_deadlines.py ~/Library/Application\ Support/CanvasDeadlines/_Tools/
```

## Schedule

`~/Library/LaunchAgents/com.yoel.canvas-deadlines.plist` — 7:00 AM and 6:00 PM.

```bash
launchctl list | grep canvas-deadlines                       # is it loaded
launchctl kickstart -k gui/$(id -u)/com.yoel.canvas-deadlines  # run now
tail -30 ~/Library/Application\ Support/CanvasDeadlines/canvas_deadlines.log
launchctl unload ~/Library/LaunchAgents/com.yoel.canvas-deadlines.plist  # stop
```

Missed runs (laptop asleep) fire once on wake — launchd does not stack them up.

## Accuracy: add an API token

Currently running on the **iCal feed**, which has two real flaws:

- Canvas emits most due dates as all-day `VALUE=DATE` entries, so **11:59 PM
  becomes 12:00 AM**. Dates are right; times are not.
- The feed has **no submission status**, so work you already turned in still
  shows as past due. Four of the five current "past due" rows are done.

Both go away with a token:

1. Canvas → Account → Settings → **+ New Access Token**
2. Paste the token *by itself* into `_Tools/canvas_token.conf` and the
   Application Support `_Tools/` copy. Gitignored in both places.
3. `chmod 600` both files.
4. Give the hosted page the same token — it is a separate credential store:

   ```bash
   gh secret set CANVAS_TOKEN < _Tools/canvas_token.conf
   gh workflow run deadlines.yml          # rebuild immediately
   ```

The script prefers the token automatically and prints `source: api`. The page
switches from "calendar feed" to "API" in its header line, times appear, and
submitted work stops showing up as past due.

Treat the token like a password: it can do anything your Canvas account can. If
it leaks, delete it from Canvas → Account → Settings and issue a new one.

## Reminders

Lead times: **3 days** and **1 day** before each due date. Each (item, threshold)
pair fires exactly once — the twice-daily schedule will not re-announce the same
quiz every run. Fired reminders are tracked in `.canvas_state.json` under
`notified` and pruned once the item passes.

```bash
python3 ... canvas_deadlines.py --lead 7 3 1     # different lead times
python3 ... canvas_deadlines.py --lead 1         # day-before only
```

To change the schedule's defaults, edit `--lead` into the plist's
`ProgramArguments`, then `launchctl unload && load`.

**These are macOS banners, so they only appear when the Mac is awake.** launchd
runs a missed job once on wake, so a closed laptop delays a reminder rather than
losing it — but if you're away from the machine for a day, the banner is not
what saves you. Canvas push is. See below.

## What Canvas itself sends

Verified 2026-08-07 for `yplutcho@student.touro.edu` and push:

| Notification | Email | Push |
|---|---|---|
| Upcoming assignment alert | daily *(was weekly)* | immediately |
| Due date changed | immediately | immediately |
| Assignment created | immediately | immediately |

Push requires the **Canvas Student** app installed and signed in — worth doing,
it is the only channel that reaches you away from the laptop.

## Secrets

`canvas_feed.conf`, `canvas_token.conf`, `.canvas_state.json` and the log are
gitignored. This repo is public at `github.com/yoelplutchok/Biochem_Fall` — the
feed URL is a bearer credential. Anyone holding it can read your whole schedule.
If it leaks, reset it in Canvas: Calendar → Calendar Feed → **Reset**.
