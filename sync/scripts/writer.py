"""Turns a normalized solved-problem record into files on disk.

Both platforms are reduced to the same two-file shape per problem:
  <root>/<platform>/<problem-dir>/solution.<ext>
  <root>/<platform>/<problem-dir>/README.md
"""

import os
import re
from datetime import datetime, timezone


def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def _fmt_date(timestamp_seconds: int) -> str:
    return datetime.fromtimestamp(int(timestamp_seconds), tz=timezone.utc).strftime("%Y-%m-%d")


def write_leetcode(root: str, record: dict) -> str:
    """record keys: slug, title, frontend_id, difficulty, tags, extension,
    code, runtime_display, memory_display, timestamp, url"""
    problem_dir = os.path.join(root, "leetcode", record["slug"])
    os.makedirs(problem_dir, exist_ok=True)

    solution_path = os.path.join(problem_dir, f"solution.{record['extension']}")
    with open(solution_path, "w") as f:
        f.write(record["code"].rstrip() + "\n")

    tags = ", ".join(record.get("tags") or [])
    readme = f"""# {record['frontend_id']}. {record['title']}

- **Difficulty:** {record.get('difficulty', 'Unknown')}
- **Tags:** {tags or 'N/A'}
- **Link:** {record['url']}
- **Last synced submission:** {_fmt_date(record['timestamp'])}
- **Runtime:** {record.get('runtime_display') or 'N/A'}
- **Memory:** {record.get('memory_display') or 'N/A'}
"""
    with open(os.path.join(problem_dir, "README.md"), "w") as f:
        f.write(readme)

    return problem_dir


def write_codeforces(root: str, record: dict) -> str:
    """record keys: contest_id, index, name, rating, tags, extension, code,
    verdict, timestamp, url"""
    dir_name = f"{record['contest_id']}{record['index']}-{_slugify(record['name'])}"
    problem_dir = os.path.join(root, "codeforces", dir_name)
    os.makedirs(problem_dir, exist_ok=True)

    solution_path = os.path.join(problem_dir, f"solution.{record['extension']}")
    with open(solution_path, "w") as f:
        f.write(record["code"].rstrip() + "\n")

    tags = ", ".join(record.get("tags") or [])
    rating = record.get("rating")
    readme = f"""# {record['contest_id']}{record['index']}. {record['name']}

- **Rating:** {rating if rating else 'Unrated'}
- **Tags:** {tags or 'N/A'}
- **Link:** {record['url']}
- **Last synced submission:** {_fmt_date(record['timestamp'])}
- **Verdict:** {record.get('verdict', 'OK')}
"""
    with open(os.path.join(problem_dir, "README.md"), "w") as f:
        f.write(readme)

    return problem_dir
