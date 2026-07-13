class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visit.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            # End case
            if r == N - 1 and c == N - 1:
                return t

            # Dfs in for directions
            for dirR, dirC in directions:
                neiR, neiC = r + dirR, c + dirC
                if ((neiR not in range(N)) or (neiC not in range(N)) or ((neiR, neiC) in visit)):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])
