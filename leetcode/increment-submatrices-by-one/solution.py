class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            prefix[row1][col1] += 1
            prefix[row2 + 1][col1] -= 1
            prefix[row1][col2 + 1] -= 1
            prefix[row2 + 1][col2 + 1] += 1

        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                x1 = 0 if i == 0 else res[i - 1][j]
                x2 = 0 if j == 0 else res[i][j - 1]
                x3 = 0 if i == 0 or j == 0 else res[i - 1][j - 1]
                res[i][j] = prefix[i][j] + x1 + x2 - x3
        return res
