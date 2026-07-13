class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        ROWS = len(board)
        COLS = len(board[0])
        nr, nc = -1, -1
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "R":
                    nr, nc = r, c
                    break
        print(nr, nc)
        res = 0
        for r in range(nr + 1, ROWS):
            if board[r][nc] == "p":
                res += 1
                break
            elif board[r][nc] != ".":
                break
        
        for r in range(nr - 1, -1, -1):
            if board[r][nc] == "p":
                res += 1
                break
            elif board[r][nc] != ".":
                break
        
        for c in range(nc + 1, COLS):
            if board[nr][c] == "p":
                res += 1
                break
            elif board[nr][c] != ".":
                break

        for c in range(nc - 1, -1, -1):
            if board[nr][c] == "p":
                res += 1
                break
            elif board[nr][c] != ".":
                break
        return res
