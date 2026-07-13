class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        map_val = defaultdict(int)
        res = [-1, -1]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                map_val[grid[i][j]] += 1

        for i in range(1, len(grid) * len(grid) + 1):
            if map_val[i] == 0:
                res[1] = i
            elif map_val[i] == 2:
                res[0] = i
        
        return res
