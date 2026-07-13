class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                on_border = row in (0, rows - 1) or col in (0, cols - 1)
                if grid[row][col] == 1 and on_border:
                    grid[row][col] = 0
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_col = row + delta_row, col + delta_col
                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 0
                    queue.append((next_row, next_col))

        return sum(cell for row in grid for cell in row)
