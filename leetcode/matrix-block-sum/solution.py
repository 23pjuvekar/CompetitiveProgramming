class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        ROWS = len(mat)
        COLS = len(mat[0])
        prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                prefix_sum[r][c] = (mat[r-1][c-1] 
                                    + prefix_sum[r-1][c] 
                                    + prefix_sum[r][c-1]
                                    - prefix_sum[r-1][c-1])
        res = [[0] * COLS for _ in range(ROWS)]
        
        def safe_idx(idx, max_val):
            return min(max(idx, 0), max_val)

        for r in range(ROWS):
            for c in range(COLS):
                r1 = safe_idx(r - k, ROWS)
                c1 = safe_idx(c - k, COLS)
                r2 = safe_idx(r + k + 1, ROWS)
                c2 = safe_idx(c + k + 1, COLS)
                res[r][c] = (prefix_sum[r2][c2] 
                             - prefix_sum[r1][c2] 
                             - prefix_sum[r2][c1] 
                             + prefix_sum[r1][c1])
        
        return res
