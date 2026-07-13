class Solution:
    def isArmstrong(self, n: int) -> bool:

        s = str(n)
        l = len(s)
        res = 0

        for c in s:
            res += (int(c) ** l)
        return res == n
