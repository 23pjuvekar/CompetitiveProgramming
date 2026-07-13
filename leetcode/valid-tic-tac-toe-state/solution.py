class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        x_count = 0
        o_count = 0
        
        for row in board:
            for char in row:
                if char == 'X':
                    x_count += 1
                elif char == 'O':
                    o_count += 1
        
        if not (x_count == o_count or x_count == o_count + 1):
            return False
        
        def is_winner(player):
            for i in range(3):
                if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                    return True
            for i in range(3):
                if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                    return True
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            if board[0][2] == player and board[1][1] == player and board[2][0] == player:
                return True
            return False
        
        x_wins = is_winner('X')
        o_wins = is_winner('O')
        
        if x_wins and o_wins:
            return False
        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and x_count != o_count:
            return False
            
        return True
