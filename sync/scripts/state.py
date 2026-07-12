"""Load/save the sync manifest that tracks the last-synced submission id per problem.

The manifest is what lets sync.py skip re-fetching source code for problems
that haven't changed since the last run. It's intentionally just a dict of
dicts keyed by a stable problem key, not by platform-specific numeric ids,
so it stays readable if you ever want to hand-edit it.
"""

import json
import os

STATE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".sync-state.json")


def load_state(path: str = STATE_PATH) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def save_state(state: dict, path: str = STATE_PATH) -> None:
    with open(path, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")


def has_changed(state: dict, problem_key: str, submission_id: str) -> bool:
    """True if this submission id hasn't been synced yet for this problem."""
    return state.get(problem_key, {}).get("submission_id") != str(submission_id)


def record(state: dict, problem_key: str, submission_id: str, synced_at: str) -> None:
    state[problem_key] = {"submission_id": str(submission_id), "synced_at": synced_at}
