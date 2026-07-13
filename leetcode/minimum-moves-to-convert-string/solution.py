class Solution:
    def minimumMoves(self, s: str) -> int:

        p = 0
        res = 0

        while p < len(s):
            if s[p] == "X":
                p += 3
                res += 1
            else:
                p += 1
        return res
