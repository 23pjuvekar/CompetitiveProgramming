class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        i = 0
        n = len(s)
        for word in words:
            for c in word:
                if i > n - 1 or s[i] != c:
                    print("h")
                    return False
                i += 1
            if i == n:
                return True
        return False
