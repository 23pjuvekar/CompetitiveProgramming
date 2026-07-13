class Solution:
    def maxPower(self, s: str) -> int:

        start = s[0]
        length = 0
        res = 1

        for c in s:
            if c == start:
                length += 1
                res = max(res, length)
            else:
                length = 1
                start = c
        return res
