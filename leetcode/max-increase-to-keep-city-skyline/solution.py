class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mc = [0] * n
        mr = [0] * n

        for r in range(n):
            for c in range(n):
                mr[r] = max(mr[r], grid[r][c])
                mc[c] = max(mc[c], grid[r][c])
        res = 0
        for r in range(n):
            for c in range(n):
                res += max(0, min(mr[r], mc[c]) - grid[r][c])
        return res
