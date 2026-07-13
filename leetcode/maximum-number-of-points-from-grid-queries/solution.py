class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        R = len(grid)
        C = len(grid[0])

        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()
        heap = [(grid[0][0], 0, 0)]
        points = 0
        visited = set()
        visited.add((0, 0))
        res = [0] * len(queries)

        for limit, index in q:
            while heap and heap[0][0] < limit:
                val, r, c = heappop(heap)
                points += 1
                neighbors = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
                for nr, nc in neighbors:
                    if (0 <= nc < C) and (0 <= nr < R) and (nr, nc) not in visited:
                        heappush(heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            res[index] = points
        return res
