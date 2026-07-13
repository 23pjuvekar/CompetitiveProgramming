class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:

        res = []
        for r in range(len(matrix)):
            res.append(sum(matrix[r]))
        return res
