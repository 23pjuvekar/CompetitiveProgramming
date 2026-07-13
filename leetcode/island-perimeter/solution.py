class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = [0]
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            res[0] += 4
            nei = [[r + 1, c], [r-1, c], [r,c+1], [r,c-1]]
            for nr, nc in nei:
                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0:
                    continue
                res[0] -= 1
                dfs(nr, nc)

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
        
        return res[0]
