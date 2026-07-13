class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            total = grid[r][c]
            for dr, dc in direction:
                nr = r + dr
                nc = c + dc
                total += dfs(nr, nc)
            return total
        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))
        return res
