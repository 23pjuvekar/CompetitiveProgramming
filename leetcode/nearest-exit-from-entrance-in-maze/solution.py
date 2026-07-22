class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        start_row, start_col = entrance

        visited = set()
        visited.add((start_row, start_col))
        queue = deque()
        queue.append((start_row, start_col, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, steps = queue.popleft()

            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col

                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                if (next_row, next_col) in visited:
                    continue
                if maze[next_row][next_col] == '+':
                    continue

                is_border = next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1
                if is_border:
                    return steps + 1

                visited.add((next_row, next_col))
                queue.append((next_row, next_col, steps + 1))

        return -1
