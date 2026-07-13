class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        o = 0
        n = len(s)
        for c in s:
            if c == "1":
                o += 1
        res = ""
        for i in range(n):
            if i <= o - 2:
                res += "1"
            elif i == n - 1:
                res += "1"
            else:
                res += "0"
        return res
