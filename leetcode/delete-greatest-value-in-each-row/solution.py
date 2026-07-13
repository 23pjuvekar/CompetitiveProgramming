class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for g in grid:
            heapify(g)
        
        res = 0
        for i in range(len(grid[0])):
            m = 0
            for g in grid:
                m = max(heappop(g), m)
            res += m
        return res
