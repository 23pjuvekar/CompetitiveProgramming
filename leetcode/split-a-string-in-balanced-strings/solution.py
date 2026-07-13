class Solution:
    def balancedStringSplit(self, s: str) -> int:

        r = 0
        l = 0
        res = 0
        for c in s:
            if c == "L":
                l += 1
            else:
                r += 1
            if l == r:
                res += 1
                l = 0
                r = 0
        return res
