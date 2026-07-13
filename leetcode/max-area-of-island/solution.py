from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxSize = 0

        def dfs(r, c):
            if (r not in range(ROWS)) or (c not in range(COLS)) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxSize = max(maxSize, dfs(r, c))
        
        return maxSize
