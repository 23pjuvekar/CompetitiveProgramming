class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
    
        ROWS = len(heightMap)
        COLS = len(heightMap[0])

        heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        
        res = 0
        max_h = -1

        while heap:
            h, r, c = heapq.heappop(heap)
            max_h = max(max_h, h)
            res += max_h - h

            nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in nei:
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or heightMap[nr][nc] == -1):
                    continue
                heapq.heappush(heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return res
