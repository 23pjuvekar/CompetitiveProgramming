class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        oro = defaultdict(int)
        oc = defaultdict(int)
        zr = defaultdict(int)
        zc = defaultdict(int)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    oro[r] += 1
                    oc[c] += 1
                else:
                    zr[r] += 1
                    zc[c] += 1
        
        res = grid.copy()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res[r][c] = oro[r] + oc[c] - zr[r] - zc[c]
        return res
