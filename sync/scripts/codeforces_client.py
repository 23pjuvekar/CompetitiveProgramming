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
        self.handle = handle.strip()
        self._session = requests.Session()
        self._session.cookies.set("JSESSIONID", session_cookie, domain="codeforces.com")
        self._session.headers.update(
            {
                "User-Agent": _BROWSER_USER_AGENT,
                "Referer": "https://codeforces.com/",
                "Accept-Language": "en-US,en;q=0.9",
            }
        )
        # Codeforces asks API consumers to stay under one call per 2 seconds.
        self._request_delay = request_delay

    def _get_status_page(self, start: int, chunk: int, retries: int = 3) -> list[dict]:
        backoff = 3.0
        last_error = None
        for attempt in range(retries):
            # Use self._session (not the bare `requests` module) so this
            # request carries the same browser User-Agent as everything
            # else — Codeforces' anti-bot layer will 400 a request that
            # looks scripted (e.g. the default "python-requests/x.y" UA)
            # even though this endpoint needs no auth at all.
            resp = self._session.get(
                API_STATUS_URL,
                params={"handle": self.handle, "from": start, "count": chunk},
                timeout=30,
            )
            if resp.status_code == 200:
                payload = resp.json()
                if payload.get("status") == "OK":
                    return payload["result"]
                last_error = f"Codeforces API error for handle '{self.handle}': {payload.get('comment')}"
            else:
                # Body matters here: Codeforces returns a JSON {"comment": ...}
                # for a real API-level problem (bad handle, bad params), but a
                # generic HTML/Cloudflare page for an IP-level block — those
                # need very different fixes, and "HTTP 400" alone can't tell
                # them apart.
                body_preview = resp.text[:300].replace("\n", " ")
                last_error = f"Codeforces API returned HTTP {resp.status_code} for user.status. Body: {body_preview!r}"

            if attempt < retries - 1:
                print(f"  [codeforces] user.status attempt {attempt + 1}/{retries} failed, retrying in {backoff:.0f}s...", flush=True)
                time.sleep(backoff)
                backoff *= 2

        raise AuthExpiredError(f"{last_error} after {retries} attempts.")

    def fetch_all_submissions(self) -> list[dict]:
        """Returns every submission (all verdicts), across paginated API calls."""
        submissions = []
        chunk = 1000
        start = 1
        while True:
            batch = self._get_status_page(start, chunk)
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
            # Diagnostic dump: could be a Cloudflare challenge page, a
            # genuine "access denied" notice, or the id we're looking for
            # having changed — the page <title> and a body snippet make it
            # obvious which, instead of guessing blind.
            title = soup.title.get_text(strip=True) if soup.title else "(no <title>)"
            body_preview = soup.get_text(" ", strip=True)[:300]
            raise AuthExpiredError(
                f"Couldn't find source code on the submission page for {submission_id} "
                f"(HTTP {resp.status_code}, page title: {title!r}, body preview: {body_preview!r})."
            )
        time.sleep(self._request_delay)
        return source_tag.get_text()
