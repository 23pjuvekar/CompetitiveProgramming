class Solution:
    def longestContinuousSubstring(self, s: str) -> int:

        curr = 1
        res = 1
        for i in range(len(s) - 1):
            if ord(s[i + 1]) - ord(s[i]) == 1:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
        return res
