class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        R = len(matrix)
        C = len(matrix[0])
        totals = [0] * C
        for r in range(1, R):
            for c in range(C):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]
        res = 0
        for r in range(R):
            matrix[r].sort()
            for c in range(C):
                res = max(res, matrix[r][c] * (C - c))
        return res
