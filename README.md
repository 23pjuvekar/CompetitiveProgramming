# CompetitiveProgramming

Automatically synced with my **latest accepted LeetCode submission** and
**latest OK Codeforces submission** for every problem I've solved, via a
daily GitHub Action. No manual copy-paste.

```
leetcode/<problem-slug>/{solution.<ext>,README.md}
codeforces/<contestId><index>-<slug>/{solution.<ext>,README.md}
sync/                         # the tooling that keeps the above up to date
```

## How it works

`sync/scripts/sync.py` runs on a daily cron (`.github/workflows/sync.yml`):

1. Pulls the full submission history from each platform.
2. Groups by problem, keeps only the newest accepted/OK submission per
   problem (`sync_leetcode` / `sync_codeforces` in `sync/scripts/sync.py`).
3. Diffs against `sync/.sync-state.json` (a committed manifest of the last
   synced submission id per problem) — unchanged problems are skipped
   entirely, so most runs do almost no network work.
4. Writes/updates `solution.<ext>` + `README.md` for anything new, commits,
   and pushes.

LeetCode has no public submissions API, so this talks to the same internal
GraphQL endpoint (`leetcode.com/graphql`) the site itself uses, authenticated
with a session cookie. Codeforces has a public API for submission metadata,
but not for source code, so source is scraped off the authenticated
submission page.

If a cookie expires, the run fails loudly (non-zero exit) instead of
silently doing nothing — GitHub emails the repo owner automatically when a
scheduled workflow run fails, so that's the "something needs attention"
signal.

## One-time setup

### 1. Get LeetCode cookies
Log into leetcode.com, open devtools → Application/Storage → Cookies, and copy:
- `LEETCODE_SESSION`
- `csrftoken`

### 2. Get the Codeforces cookie
Log into codeforces.com, open devtools → Application/Storage → Cookies, and copy:
- `JSESSIONID`

These are session cookies, not passwords — they expire periodically (weeks
to months), at which point the workflow starts failing and emails you; just
repeat these two steps and update the secrets below.

### 3. Add repo secrets
Settings → Secrets and variables → Actions:
| Secret | Value |
|---|---|
| `LEETCODE_SESSION` | from step 1 |
| `LEETCODE_CSRF_TOKEN` | the `csrftoken` cookie from step 1 |
| `CF_HANDLE` | Codeforces username |
| `CF_SESSION` | the `JSESSIONID` cookie from step 2 |

### 4. Enable write permissions for the workflow
Settings → Actions → General → Workflow permissions → **Read and write permissions**.

### 5. Test it
Actions tab → "Sync solutions" → Run workflow (manual `workflow_dispatch`
trigger). After that it runs automatically every day at 06:00 UTC.

## Local development

```bash
cd sync
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export LEETCODE_SESSION=...
export LEETCODE_CSRF_TOKEN=...
export CF_HANDLE=...
export CF_SESSION=...

python scripts/sync.py --dry-run   # preview only, no writes/commits
python scripts/sync.py             # real run
```

Run tests with `pytest sync/tests/` from the repo root (no credentials
needed — they use fake clients to test the dedup/grouping logic in
isolation).
