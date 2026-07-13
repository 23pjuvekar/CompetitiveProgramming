class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        res = 0
        for g in grid:
            l = 0
            r = len(g) - 1
            while l <= r:
                m = (l + r) // 2
                if g[m] < 0:
                    r = m - 1
                else:
                    l = m + 1
            res += (len(g) - l)
        return res
