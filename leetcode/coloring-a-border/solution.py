class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        seen = set()
        rows, cols = len(grid), len(grid[0])
        original_color = grid[r0][c0]

        def dfs(x, y):
            if (x, y) in seen:
                return True
    
            is_in_bounds = 0 <= x < rows and 0 <= y < cols
            if not is_in_bounds or grid[x][y] != original_color:
                return False

            seen.add((x, y))

            all_neighbors_in_component = (
                dfs(x + 1, y)
                + dfs(x - 1, y)
                + dfs(x, y + 1)
                + dfs(x, y - 1)
            ) == 4

            if not all_neighbors_in_component:
                grid[x][y] = color

            return True

        dfs(r0, c0)
        return grid
