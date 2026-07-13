class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        n = len(grid)
        res = 0
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for r in range(n):
            for c in range(n):
                if grid[r][c] > 0:
                    res += 2
                for nr, nc in direction:
                    if 0 <= nr + r < n and 0 <= nc + c < n:
                        res += max(0, grid[r][c] - grid[nr + r][nc + c])
                    else:
                        res += grid[r][c]
        return res
