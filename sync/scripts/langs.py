"""Maps platform-reported language names to file extensions."""

LEETCODE_EXTENSIONS = {
    "python": "py",
    "python3": "py",
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "java": "java",
    "javascript": "js",
    "typescript": "ts",
    "php": "php",
    "swift": "swift",
    "kotlin": "kt",
    "dart": "dart",
    "golang": "go",
    "ruby": "rb",
    "scala": "scala",
    "rust": "rs",
    "racket": "rkt",
    "erlang": "erl",
    "elixir": "ex",
    "mysql": "sql",
    "mssql": "sql",
    "oraclesql": "sql",
    "postgresql": "sql",
    "pythondata": "py",
    "bash": "sh",
}

CODEFORCES_EXTENSIONS = {
    "gnu c": "c",
    "gnu c11": "c",
    "gnu c++": "cpp",
    "gnu c++11": "cpp",
    "gnu c++14": "cpp",
    "gnu c++17": "cpp",
    "gnu c++17 (64_bit, msys 2)": "cpp",
    "gnu c++20": "cpp",
    "gnu c++23": "cpp",
    "ms c++": "cpp",
    "ms c++ 2017": "cpp",
    "python 2": "py",
    "python 3": "py",
    "pypy 2": "py",
    "pypy 3": "py",
    "pypy 3-64": "py",
    "java 8": "java",
    "java 11": "java",
    "java 17": "java",
    "java 21": "java",
    "kotlin": "kt",
    "kotlin 1.6": "kt",
    "kotlin 1.7": "kt",
    "go": "go",
    "rust": "rs",
    "rust 2021": "rs",
    "javascript": "js",
    "node.js": "js",
    "typescript": "ts",
    "c#": "cs",
    "c# 8": "cs",
    "c# 10": "cs",
    "mono c#": "cs",
    "php": "php",
    "ruby": "rb",
    "scala": "scala",
    "haskell": "hs",
    "perl": "pl",
    "d": "d",
    "ocaml": "ml",
}


def leetcode_extension(lang: str) -> str:
    return LEETCODE_EXTENSIONS.get(lang.lower().strip(), "txt")


def codeforces_extension(lang: str) -> str:
    key = lang.lower().strip()
    if key in CODEFORCES_EXTENSIONS:
        return CODEFORCES_EXTENSIONS[key]
    # Codeforces language strings carry version suffixes we don't enumerate
    # (e.g. "GNU C++17 (64_bit, msys 2)") — fall back to a prefix match.
    for known, ext in CODEFORCES_EXTENSIONS.items():
        if key.startswith(known):
            return ext
    return "txt"
