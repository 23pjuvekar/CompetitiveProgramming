class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = defaultdict(int)
        for r in grid:
            rows[tuple(r)] += 1
        res = 0

        for i in range(len(grid[0])):
            curr = []
            for j in range(len(grid)):
                curr.append(grid[j][i])
            res += rows[tuple(curr)]
        return res
