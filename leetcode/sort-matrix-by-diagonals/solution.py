class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        d = defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                d[r - c].append(grid[r][c])
            
        for key, val in d.items():
            if key >= 0:
                val.sort()
            else:
                val.sort(reverse=True)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = d[r - c].pop()
        return grid
