# DFS from each part of land turning each part of land that touches a side to water
# DFS on center part now counting island theres

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        # Globals
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        res = 0

        def dfs_wc(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return # Exit if out of bounds
            if grid[r][c] == 0: # If land
                grid[r][c] = 1
                dfs_wc(r + 1, c)
                dfs_wc(r - 1, c)
                dfs_wc(r, c + 1)
                dfs_wc(r, c - 1)

        def dfs_count_islands(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return # Exit if out of bounds

            if grid[r][c] == 1 or (r, c) in visit:
                return # Already counted

            visit.add((r, c))

            dfs_count_islands(r + 1, c)
            dfs_count_islands(r - 1, c)
            dfs_count_islands(r, c + 1)
            dfs_count_islands(r, c - 1)

            



    

        # Sides Islands into water DFS
        for r in range(ROWS):
            dfs_wc(r, 0)
            dfs_wc(r, COLS - 1)

        # Top and bottom Islands into water DFS
        for c in range(COLS):
            dfs_wc(0, c)
            dfs_wc(ROWS - 1, c)

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if grid[r][c] == 0 and (r, c) not in visit:
                    res += 1
                    dfs_count_islands(r, c)

    
        return res
