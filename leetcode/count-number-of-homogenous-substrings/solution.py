class Solution:
    def countHomogenous(self, s: str) -> int:

        # 1 + 2 + n = ((n + 1) * n) / 2

        l = 0
        res = 0
        while l < len(s):
            r = l
            while r < len(s) and s[l] == s[r]:
                r += 1
            n = r - l
            res += ((n + 1) * n) // 2
            res = res % (10**9 + 7)
            l = r
        return res % (10**9 + 7)
