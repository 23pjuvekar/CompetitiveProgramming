class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        best_health = [[-1] * cols for _ in range(rows)]
        best_health[0][0] = health - grid[0][0]
        queue = deque([(0, 0)])

        while queue:
            r, c = queue.popleft()
            current_health = best_health[r][c]

            if (r, c) == (rows - 1, cols - 1):
                return current_health > 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                new_health = current_health - grid[nr][nc]
                if new_health > best_health[nr][nc]:
                    best_health[nr][nc] = new_health
                    if grid[nr][nc] == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))

        return False
