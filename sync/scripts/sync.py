#!/usr/bin/env python3
"""Entry point: pulls the latest accepted submission per problem from LeetCode
and Codeforces, writes/updates files in this repo, and commits the result.

Usage:
    python sync/scripts/sync.py              # real run, writes files + commits
    python sync/scripts/sync.py --dry-run    # prints what would change, no writes

Credentials come from environment variables (set as GitHub Actions secrets
in CI, or exported locally for testing):
    LEETCODE_SESSION, LEETCODE_CSRF_TOKEN
    CF_HANDLE, CF_SESSION
A platform is skipped (not treated as an error) if its env vars are simply
unset. If they're set but the site rejects them, that's a real
AuthExpiredError and the script exits non-zero so CI surfaces a failure.
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import langs
import state as state_mod
import writer
from codeforces_client import AuthExpiredError as CFAuthError
from codeforces_client import CodeforcesClient
from leetcode_client import AuthExpiredError as LCAuthError
from leetcode_client import LeetCodeClient

# __file__ is sync/scripts/sync.py — go up three levels to the actual repo
# root, since leetcode/ and codeforces/ solution folders live there, not
# nested under sync/ alongside the tooling.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def sync_leetcode(client: LeetCodeClient, state: dict, dry_run: bool) -> int:
    submissions = client.fetch_all_submissions()
    accepted = [s for s in submissions if s.get("statusDisplay") == "Accepted"]

    latest_by_slug = {}
    for s in accepted:
        slug = s["titleSlug"]
        if slug not in latest_by_slug or int(s["timestamp"]) > int(latest_by_slug[slug]["timestamp"]):
            latest_by_slug[slug] = s

    changed = 0
    for slug, submission in latest_by_slug.items():
        problem_key = f"leetcode:{slug}"
        if not state_mod.has_changed(state, problem_key, submission["id"]):
            continue

        print(f"[leetcode] syncing {slug} (submission {submission['id']})")
        details = client.fetch_submission_source(submission["id"])
        meta = client.fetch_question_meta(slug)
        lang_name = details.get("lang", {}).get("name", submission.get("lang", ""))

        record = {
            "slug": slug,
            "title": meta.get("title", submission.get("title", slug)),
            "frontend_id": meta.get("questionFrontendId", "?"),
            "difficulty": meta.get("difficulty"),
            "tags": [t["name"] for t in meta.get("topicTags", [])],
            "extension": langs.leetcode_extension(lang_name),
            "code": details["code"],
            "runtime_display": details.get("runtimeDisplay"),
            "memory_display": details.get("memoryDisplay"),
            "timestamp": submission["timestamp"],
            "url": f"https://leetcode.com/problems/{slug}/",
        }

        if not dry_run:
            writer.write_leetcode(ROOT, record)
            state_mod.record(
                state,
                problem_key,
                submission["id"],
                datetime.now(timezone.utc).isoformat(),
            )
        changed += 1

    return changed


def sync_codeforces(client: CodeforcesClient, state: dict, dry_run: bool) -> int:
    submissions = client.fetch_all_submissions()
    accepted = [s for s in submissions if s.get("verdict") == "OK"]

    latest_by_problem = {}
    for s in accepted:
        problem = s["problem"]
        key = f"{problem['contestId']}{problem.get('index', '')}"
        if key not in latest_by_problem or int(s["creationTimeSeconds"]) > int(
            latest_by_problem[key]["creationTimeSeconds"]
        ):
            latest_by_problem[key] = s

    changed = 0
    for key, submission in latest_by_problem.items():
        problem_key = f"codeforces:{key}"
        if not state_mod.has_changed(state, problem_key, submission["id"]):
            continue

        print(f"[codeforces] syncing {key} (submission {submission['id']})")
        problem = submission["problem"]
        source = client.fetch_submission_source(problem["contestId"], submission["id"])

        record = {
            "contest_id": problem["contestId"],
            "index": problem.get("index", ""),
            "name": problem.get("name", key),
            "rating": problem.get("rating"),
            "tags": problem.get("tags", []),
            "extension": langs.codeforces_extension(submission.get("programmingLanguage", "")),
            "code": source,
            "verdict": submission.get("verdict"),
            "timestamp": submission["creationTimeSeconds"],
            "url": f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem.get('index', '')}",
        }

        if not dry_run:
            writer.write_codeforces(ROOT, record)
            state_mod.record(
                state,
                problem_key,
                submission["id"],
                datetime.now(timezone.utc).isoformat(),
            )
        changed += 1

    return changed


def commit_and_push(total_changed: int) -> None:
    if total_changed == 0:
        print("Nothing changed, skipping commit.")
        return
    if not os.path.isdir(os.path.join(ROOT, ".git")):
        print("Not a git repo (or .git missing) — skipping commit.")
        return

    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout
    if not status.strip():
        print("git status is clean, skipping commit.")
        return

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    message = f"Sync: {total_changed} problem(s) updated ({date_str})"
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
    subprocess.run(["git", "push"], cwd=ROOT, check=True)
    print(f"Committed and pushed: {message}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Don't write files, save state, or commit.")
    args = parser.parse_args()

    state = state_mod.load_state()
    total_changed = 0

    lc_session = os.environ.get("LEETCODE_SESSION", "")
    lc_csrf = os.environ.get("LEETCODE_CSRF_TOKEN", "")
    if lc_session and lc_csrf:
        try:
            client = LeetCodeClient(lc_session, lc_csrf)
            total_changed += sync_leetcode(client, state, args.dry_run)
        except LCAuthError as e:
            print(f"ERROR [leetcode]: {e}", file=sys.stderr)
            return 1
    else:
        print("Skipping LeetCode (LEETCODE_SESSION / LEETCODE_CSRF_TOKEN not set).")

    cf_handle = os.environ.get("CF_HANDLE", "")
    cf_session = os.environ.get("CF_SESSION", "")
    if cf_handle and cf_session:
        try:
            client = CodeforcesClient(cf_handle, cf_session)
            total_changed += sync_codeforces(client, state, args.dry_run)
        except CFAuthError as e:
            print(f"ERROR [codeforces]: {e}", file=sys.stderr)
            return 1
    else:
        print("Skipping Codeforces (CF_HANDLE / CF_SESSION not set).")

    if args.dry_run:
        print(f"\nDry run complete. {total_changed} problem(s) would be synced.")
        return 0

    state_mod.save_state(state)
    print(f"\nSynced {total_changed} problem(s).")
    commit_and_push(total_changed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
