class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        rows_c = []
        cols_c = []
        for r in range(len(mat)):
            if sum(mat[r]) == 1:
                rows_c.append(r)
            
        for c in range(len(mat[0])):
            curr = 0
            for r in range(len(mat)):
                curr += mat[r][c]
            if curr == 1:
                cols_c.append(c)
        res = 0
        for r in rows_c:
            for c in cols_c:
                if mat[r][c] == 1:
                    res += 1
        return res
