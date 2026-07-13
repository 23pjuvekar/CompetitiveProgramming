class Solution(object):
    def isToeplitzMatrix(self, matrix):
        
        for r in range(len(matrix)):
            row = matrix[r]
            for c in range(len(row)):
                val = row[c]
                if r == 0 or c == 0 or matrix[r-1][c-1] == val:
                    continue
                else:
                    return False
        return True
