class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowMin = []
        for r in range(ROWS):
            rMin = float('inf')
            for c in range(COLS):
                rMin = min(rMin, matrix[r][c])
            rowMin.append(rMin)
        
        colMax = []
        for c in range(COLS):
            cMax = float('-inf')
            for r in range(ROWS):
                cMax = max(cMax, matrix[r][c])
            colMax.append(cMax)

        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == rowMin[r] and matrix[r][c] == colMax[c]:
                    res.append(matrix[r][c])
        
        return res
