class Solution:
    def thousandSeparator(self, n: int) -> str:

        n = str(n)[::-1]
        res = ""
        cnt = 0
        for c in n:
            res += c
            cnt += 1
            if cnt % 3 == 0 and cnt != len(n):
                res += "."
        return res[::-1]
