"""Client for Codeforces submission data.

Metadata (verdict, problem, language, timestamp) comes from the official
public API — no auth needed. Source code is NOT exposed by that API, so
it's scraped off the authenticated submission page using a logged-in
JSESSIONID cookie, same trick tools like cf-tool use for pulling your own
past submissions.
"""

import time

import requests
from bs4 import BeautifulSoup

API_STATUS_URL = "https://codeforces.com/api/user.status"
SUBMISSION_PAGE_URL = "https://codeforces.com/contest/{contest_id}/submission/{submission_id}"

_BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


class AuthExpiredError(Exception):
    """Raised when the Codeforces session cookie is missing, invalid, or expired."""


class CodeforcesClient:
    def __init__(self, handle: str, session_cookie: str, request_delay: float = 2.0):
        if not handle:
            raise AuthExpiredError("CF_HANDLE not set.")
        if not session_cookie:
            raise AuthExpiredError(
                "CF_SESSION (JSESSIONID) not set. Grab a fresh cookie from codeforces.com devtools "
                "and update the repo secret."
            )
        self.handle = handle
        self._session = requests.Session()
        self._session.cookies.set("JSESSIONID", session_cookie, domain="codeforces.com")
        self._session.headers.update({"User-Agent": _BROWSER_USER_AGENT})
        # Codeforces asks API consumers to stay under one call per 2 seconds.
        self._request_delay = request_delay

    def fetch_all_submissions(self) -> list[dict]:
        """Returns every submission (all verdicts), across paginated API calls."""
        submissions = []
        chunk = 1000
        start = 1
        while True:
            resp = requests.get(
                API_STATUS_URL,
                params={"handle": self.handle, "from": start, "count": chunk},
                timeout=30,
            )
            resp.raise_for_status()
            payload = resp.json()
            if payload.get("status") != "OK":
                raise AuthExpiredError(f"Codeforces API error for handle '{self.handle}': {payload.get('comment')}")
            batch = payload["result"]
            submissions.extend(batch)
            if len(batch) < chunk:
                break
            start += chunk
            time.sleep(self._request_delay)
        return submissions

    def fetch_submission_source(self, contest_id: int, submission_id: str) -> str:
        url = SUBMISSION_PAGE_URL.format(contest_id=contest_id, submission_id=submission_id)
        resp = self._session.get(url, timeout=30)
        if resp.status_code in (401, 403):
            raise AuthExpiredError(f"Codeforces returned HTTP {resp.status_code} fetching submission {submission_id}.")
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")
        if soup.select_one("#enterForm") is not None:
            raise AuthExpiredError(
                f"Codeforces redirected to login while fetching submission {submission_id} — "
                "CF_SESSION cookie is likely expired."
            )
        source_tag = soup.select_one("#program-source-text")
        if source_tag is None:
            raise AuthExpiredError(
                f"Couldn't find source code on the submission page for {submission_id} "
                "(page layout changed, or the session is no longer valid)."
            )
        time.sleep(self._request_delay)
        return source_tag.get_text()
