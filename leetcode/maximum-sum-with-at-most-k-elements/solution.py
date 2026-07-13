class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        res = []
        for i in range(len(grid)):
            row = grid[i]
            row.sort(reverse=True)
            for x in range(limits[i]):
                res.append(row[x])
        
        res.sort(reverse=True)
        return sum(res[:k])
