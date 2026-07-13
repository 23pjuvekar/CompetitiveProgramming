class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        q = deque()
        q.append((0, 0))
        visited = set((0, 0))
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        n = len(grid)

        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        distance = 1
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if (x, y) == (n-1, n-1):
                    return distance
                for cx, cy in directions:
                    nx = x + cx
                    ny = y + cy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            distance += 1
        
        return -1
