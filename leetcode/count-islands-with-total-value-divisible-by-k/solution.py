class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        seen = set()
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0 or (r, c) in seen:
                return 0
            seen.add((r, c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + grid[r][c]
        
        res = 0
        for r in range(R):
            for c in range(C):
                if (r, c) not in seen and grid[r][c] != 0:
                    if dfs(r, c) % k == 0:
                        res += 1 
        return res
