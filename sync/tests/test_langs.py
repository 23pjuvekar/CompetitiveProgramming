import langs


def test_leetcode_known_language():
    assert langs.leetcode_extension("python3") == "py"
    assert langs.leetcode_extension("Cpp") == "cpp"


def test_leetcode_unknown_language_falls_back_to_txt():
    assert langs.leetcode_extension("some-future-lang") == "txt"


def test_codeforces_exact_match():
    assert langs.codeforces_extension("GNU C++17") == "cpp"
    assert langs.codeforces_extension("PyPy 3") == "py"


def test_codeforces_versioned_variant_falls_back_to_prefix_match():
    # Codeforces appends build info we don't enumerate explicitly.
    assert langs.codeforces_extension("GNU C++17 (64_bit, msys 2)") == "cpp"


def test_codeforces_unknown_language_falls_back_to_txt():
    assert langs.codeforces_extension("some-future-lang") == "txt"
