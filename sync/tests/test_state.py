import os

import state as state_mod


def test_has_changed_true_for_unknown_problem():
    assert state_mod.has_changed({}, "leetcode:two-sum", "123")


def test_has_changed_false_after_recording_same_submission():
    s = {}
    state_mod.record(s, "leetcode:two-sum", "123", "2026-01-01T00:00:00Z")
    assert not state_mod.has_changed(s, "leetcode:two-sum", "123")


def test_has_changed_true_when_submission_id_differs():
    s = {}
    state_mod.record(s, "leetcode:two-sum", "123", "2026-01-01T00:00:00Z")
    assert state_mod.has_changed(s, "leetcode:two-sum", "456")


def test_save_and_load_round_trip(tmp_path):
    path = os.path.join(tmp_path, ".sync-state.json")
    s = {}
    state_mod.record(s, "codeforces:1000A", "999", "2026-01-01T00:00:00Z")
    state_mod.save_state(s, path=path)

    loaded = state_mod.load_state(path=path)
    assert loaded == s
    assert not state_mod.has_changed(loaded, "codeforces:1000A", "999")


def test_load_state_missing_file_returns_empty_dict(tmp_path):
    path = os.path.join(tmp_path, "does-not-exist.json")
    assert state_mod.load_state(path=path) == {}
