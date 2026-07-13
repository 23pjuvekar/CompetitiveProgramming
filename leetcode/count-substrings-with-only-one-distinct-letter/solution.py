class Solution:
    def countLetters(self, s: str) -> int:

        res = 0
        l = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                res += ((r - l) * (r - l + 1)) // 2
                l = r
        res += ((r - l + 2) * (r - l + 1)) // 2
        return res
