class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                total += grid[r][c]

        curr_total = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                curr_total += grid[r][c]
            if curr_total == total / 2:
                return True

        curr_total = 0
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                curr_total += grid[r][c]
            if curr_total == total / 2:
                return True
        
        return False
