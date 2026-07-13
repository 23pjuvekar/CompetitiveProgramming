class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        new = [[0] * len(matrix) for row in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                new[c][r] = matrix[r][c]
        return new
