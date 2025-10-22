class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        diag_neg = set() # r - c
        diag_pos = set() # r + c

        res = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in diag_pos or (r - c) in diag_neg:
                    continue
                
                cols.add(c)
                diag_neg.add(r - c)
                diag_pos.add(r + c)
                board[r][c] = "Q"

                dfs(r + 1)

                cols.remove(c)
                diag_neg.remove(r - c)
                diag_pos.remove(r + c)
                board[r][c] = "."
        
        dfs(0)
        return res