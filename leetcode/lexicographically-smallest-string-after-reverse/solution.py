class Solution:
    def lexSmallest(self, s: str) -> str:

        res = s

        for i in range(len(s)):
            res = min(res, s[:i][::-1] + s[i:])
            res = min(res, s[:i] + s[i:][::-1])
        return res
