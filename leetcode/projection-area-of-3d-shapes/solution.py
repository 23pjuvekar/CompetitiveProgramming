class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        max_rows = [0] * N
        max_cols = [0] * N
        res = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] != 0:
                    res += 1
                max_rows[r] = max(max_rows[r], grid[r][c])
                max_cols[c] = max(max_cols[c], grid[r][c])
        
        return res + sum(max_rows) + sum(max_cols)
