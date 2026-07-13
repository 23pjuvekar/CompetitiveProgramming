class Solution:
    def captureForts(self, f: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(f)):
            if f[r] != 0:
                if (f[l] == 1 and f[r] == -1) or (f[l] == -1 and f[r] ==1):
                    res = max(res, r - l - 1)
                l = r
        return res
