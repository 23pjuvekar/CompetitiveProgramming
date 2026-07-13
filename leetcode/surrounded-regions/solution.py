class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if (r not in range(ROWS)) or (c not in range(COLS)) or (board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Turn any unsurrounded O's into T
        # Rows edge
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # Columns edge
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        # Turn any O's into X and T into O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
