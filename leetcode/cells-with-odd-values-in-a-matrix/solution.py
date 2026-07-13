class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res = [[0] * n for _ in range(m)]
        
        for r, c in indices:
            for i in range(n):
                res[r][i] += 1
            for i in range(m):
                res[i][c] += 1
        res_f = 0
        for row in res:
            for c in row:
                if c % 2 == 1:
                    res_f += 1
        return res_f
