class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        ROWS = len(mat)
        COLS = len(mat[0])

        if ROWS * COLS != r * c:
            return mat

        res = [[0 for j in range(c)] for i in range(r)]

        for i in range(ROWS * COLS):
            res[i // c][i % c] = mat[i // COLS][i % COLS]
        
        return res
