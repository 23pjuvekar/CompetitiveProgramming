class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(n):
                    matrix[r][c] = 0
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(m):
                    matrix[r][c] = 0
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0
