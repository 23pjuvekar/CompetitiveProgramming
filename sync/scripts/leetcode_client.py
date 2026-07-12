"""Client for LeetCode's internal GraphQL API.

LeetCode has no public API for personal submission history, but the site
itself talks to https://leetcode.com/graphql using a logged-in session
cookie. That's what we piggyback on here — same approach used by
joshcai/leetcode-sync and similar tools, reimplemented directly so we
control the file layout and dedup logic ourselves.
"""

import time

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

_SUBMISSION_LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
    lastKey
    hasNext
    submissions {
      id
      titleSlug
      title
      statusDisplay
      lang
      timestamp
    }
  }
}
"""

_SUBMISSION_DETAILS_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    lang {
      name
    }
    runtimeDisplay
    memoryDisplay
    timestamp
  }
}
"""

_QUESTION_META_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    topicTags {
      name
    }
  }
}
"""


class AuthExpiredError(Exception):
    """Raised when the LeetCode session cookie is missing, invalid, or expired."""


class LeetCodeClient:
    def __init__(self, session_cookie: str, csrf_token: str, request_delay: float = 0.4):
        if not session_cookie or not csrf_token:
            raise AuthExpiredError(
                "LEETCODE_SESSION / LEETCODE_CSRF_TOKEN not set. "
                "Grab fresh cookies from leetcode.com devtools and update the repo secrets."
            )
        self._session = requests.Session()
        self._session.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
        self._session.cookies.set("csrftoken", csrf_token, domain="leetcode.com")
        self._session.headers.update(
            {
                "Content-Type": "application/json",
                "Referer": "https://leetcode.com",
                "x-csrftoken": csrf_token,
                "User-Agent": "Mozilla/5.0 (algo-solutions sync bot)",
            }
        )
        self._request_delay = request_delay
        self._question_meta_cache: dict[str, dict] = {}

    def _post(self, query: str, variables: dict, operation_name: str) -> dict:
        resp = self._session.post(
            GRAPHQL_URL,
            json={"query": query, "variables": variables, "operationName": operation_name},
            timeout=30,
        )
        if resp.status_code in (401, 403):
            raise AuthExpiredError(
                f"LeetCode returned HTTP {resp.status_code} on '{operation_name}' — "
                "the session cookie is almost certainly expired."
            )
        resp.raise_for_status()
        payload = resp.json()
        if payload.get("errors"):
            raise AuthExpiredError(f"LeetCode GraphQL errors on '{operation_name}': {payload['errors']}")
        data = payload.get("data") or {}
        # An empty/null top-level result on an authenticated query almost
        # always means the session cookie no longer maps to a logged-in user.
        if all(v is None for v in data.values()):
            raise AuthExpiredError(
                f"LeetCode returned no data for '{operation_name}' — session cookie is likely expired."
            )
        return data

    def fetch_all_submissions(self) -> list[dict]:
        """Returns every submission (all statuses), newest first."""
        submissions = []
        offset = 0
        limit = 20
        last_key = None
        while True:
            data = self._post(
                _SUBMISSION_LIST_QUERY,
                {"offset": offset, "limit": limit, "lastKey": last_key},
                "submissionList",
            )
            block = data["submissionList"]
            submissions.extend(block["submissions"])
            if not block.get("hasNext"):
                break
            offset += limit
            last_key = block.get("lastKey")
            time.sleep(self._request_delay)
        return submissions

    def fetch_submission_source(self, submission_id: str) -> dict:
        data = self._post(
            _SUBMISSION_DETAILS_QUERY,
            {"submissionId": int(submission_id)},
            "submissionDetails",
        )
        details = data.get("submissionDetails")
        if not details:
            raise AuthExpiredError(f"No submissionDetails returned for submission {submission_id}.")
        time.sleep(self._request_delay)
        return details

    def fetch_question_meta(self, title_slug: str) -> dict:
        if title_slug in self._question_meta_cache:
            return self._question_meta_cache[title_slug]
        data = self._post(_QUESTION_META_QUERY, {"titleSlug": title_slug}, "questionData")
        meta = data.get("question") or {}
        self._question_meta_cache[title_slug] = meta
        time.sleep(self._request_delay)
        return meta
