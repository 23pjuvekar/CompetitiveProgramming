class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l_c = 0
        r_c = COLS - 1
        t_r = 0
        b_r = ROWS - 1
        res = []

        while True:
            for c in range(l_c, r_c + 1):
                res.append(matrix[t_r][c])
                if len(res) == ROWS * COLS:
                    return res
            t_r += 1

            for r in range(t_r, b_r + 1):
                res.append(matrix[r][r_c])
                if len(res) == ROWS * COLS:
                    return res
            r_c -= 1


            for c in reversed(range(l_c, r_c + 1)):
                res.append(matrix[b_r][c])
                if len(res) == ROWS * COLS:
                    return res
            b_r -= 1


            for r in reversed(range(t_r, b_r + 1)):
                res.append(matrix[r][l_c])
                if len(res) == ROWS * COLS:
                    return res
            l_c += 1

        
        return res
