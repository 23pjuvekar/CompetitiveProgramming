class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if r + 1 != m and grid[r][c] != grid[r + 1][c]:
                    return False
                if c + 1 != n and grid[r][c] == grid[r][c + 1]:
                    return False
        
        return True
