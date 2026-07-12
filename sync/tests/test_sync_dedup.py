"""Verifies the 'latest valid submission per problem' rule and the
skip-if-unchanged behavior, using fake clients so no network calls happen.
"""

import os

import sync


class FakeLeetCodeClient:
    def fetch_all_submissions(self):
        return [
            {"id": "1", "titleSlug": "two-sum", "title": "Two Sum", "statusDisplay": "Wrong Answer", "lang": "python3", "timestamp": "100"},
            {"id": "2", "titleSlug": "two-sum", "title": "Two Sum", "statusDisplay": "Accepted", "lang": "python3", "timestamp": "200"},
            {"id": "3", "titleSlug": "two-sum", "title": "Two Sum", "statusDisplay": "Accepted", "lang": "python3", "timestamp": "300"},
        ]

    def fetch_submission_source(self, submission_id):
        return {
            "code": f"# solution for submission {submission_id}",
            "lang": {"name": "python3"},
            "runtimeDisplay": "40 ms",
            "memoryDisplay": "10 MB",
        }

    def fetch_question_meta(self, slug):
        return {
            "title": "Two Sum",
            "questionFrontendId": "1",
            "difficulty": "Easy",
            "topicTags": [{"name": "Array"}, {"name": "Hash Table"}],
        }


class FakeCodeforcesClient:
    def fetch_all_submissions(self):
        problem = {"contestId": 1000, "index": "A", "name": "Sample Problem", "rating": 800, "tags": ["math"]}
        return [
            {"id": "10", "problem": problem, "verdict": "WRONG_ANSWER", "creationTimeSeconds": 100, "programmingLanguage": "GNU C++17"},
            {"id": "11", "problem": problem, "verdict": "OK", "creationTimeSeconds": 200, "programmingLanguage": "GNU C++17"},
            {"id": "12", "problem": problem, "verdict": "OK", "creationTimeSeconds": 300, "programmingLanguage": "GNU C++17"},
        ]

    def fetch_submission_source(self, contest_id, submission_id):
        return f"// solution for submission {submission_id}"


def test_leetcode_picks_latest_accepted_submission(tmp_path, monkeypatch):
    monkeypatch.setattr(sync, "ROOT", str(tmp_path))
    state = {}

    changed = sync.sync_leetcode(FakeLeetCodeClient(), state, dry_run=False)

    assert changed == 1
    solution_path = tmp_path / "leetcode" / "two-sum" / "solution.py"
    assert solution_path.exists()
    assert "submission 3" in solution_path.read_text()
    assert state["leetcode:two-sum"]["submission_id"] == "3"


def test_leetcode_skips_when_already_synced(tmp_path, monkeypatch):
    monkeypatch.setattr(sync, "ROOT", str(tmp_path))
    state = {"leetcode:two-sum": {"submission_id": "3", "synced_at": "x"}}

    changed = sync.sync_leetcode(FakeLeetCodeClient(), state, dry_run=False)

    assert changed == 0
    assert not (tmp_path / "leetcode").exists()


def test_codeforces_picks_latest_ok_submission(tmp_path, monkeypatch):
    monkeypatch.setattr(sync, "ROOT", str(tmp_path))
    state = {}

    changed = sync.sync_codeforces(FakeCodeforcesClient(), state, dry_run=False)

    assert changed == 1
    solution_path = tmp_path / "codeforces" / "1000A-sample-problem" / "solution.cpp"
    assert solution_path.exists()
    assert "submission 12" in solution_path.read_text()
    assert state["codeforces:1000A"]["submission_id"] == "12"


def test_dry_run_does_not_write_files_or_state(tmp_path, monkeypatch):
    monkeypatch.setattr(sync, "ROOT", str(tmp_path))
    state = {}

    changed = sync.sync_leetcode(FakeLeetCodeClient(), state, dry_run=True)

    assert changed == 1
    assert not (tmp_path / "leetcode").exists()
    assert state == {}
