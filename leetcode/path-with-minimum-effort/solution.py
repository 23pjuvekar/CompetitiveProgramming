class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        efforts = [[float('inf')] * m for _ in range(n)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            current_effort, r, c = heapq.heappop(pq)
            if current_effort > efforts[r][c]:
                continue
            if r == n - 1 and c == m - 1:
                return current_effort
            for dr, dc in self.dir:
                nr, nc = r + dr, c + dc
                if self.isValidCell(heights, nr, nc):
                    edge_effort = abs(heights[r][c] - heights[nr][nc])
                    new_max_effort = max(current_effort, edge_effort)
                    if new_max_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_max_effort
                        heapq.heappush(pq, (new_max_effort, nr, nc))
        return efforts[n - 1][m - 1]

    def isValidCell(self, heights, i, j) -> bool:
        n = len(heights)
        m = len(heights[0])
        return 0 <= i < n and 0 <= j < m
