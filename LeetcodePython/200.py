class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def dfs(x, y):
            if x < 0 or x == ROWS or y < 0 or y == COLS or (x, y) in visited or grid[x][y] == "0":
                return
        
            visited.add((x, y))

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == "1" and (x, y) not in visited:
                    res += 1
                    dfs(x, y)

        return res
            

        
        