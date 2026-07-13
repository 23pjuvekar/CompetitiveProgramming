class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p_ocean = set()
        a_ocean = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, visited, before_height):
            if r not in range(ROWS) or c not in range(COLS) or before_height > heights[r][c] or (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        # Top and Bottom COLUMNS
        for r in range(ROWS):
            dfs(r, 0, p_ocean, heights[r][0])
            dfs(r, COLS - 1, a_ocean, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, p_ocean, heights[0][c])
            dfs(ROWS - 1, c, a_ocean, heights[ROWS - 1][c])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p_ocean and (r, c) in a_ocean:
                    res.append([r, c])

        return res
