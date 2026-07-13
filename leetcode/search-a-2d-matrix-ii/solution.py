class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        for row in matrix:
            index = bisect_left(row, target)
            if index >= len(row) or row[index] != target:
                continue
            else:
                return True
        """

        r = 0
        c = len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
        return False
