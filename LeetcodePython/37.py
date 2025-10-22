import collections

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boards = defaultdict(set)
        empty = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boards[(r // 3, c // 3)].add(board[r][c])
        
        def bt(i):
            if i >= len(empty):
                return True
            
            r, c = empty[i]
            for x in "123456789":
                if x not in rows[r] and x not in cols[c] and x not in boards[(r // 3, c // 3)]:
                    board[r][c] = x
                    rows[r].add(x)
                    cols[c].add(x)
                    boards[(r // 3, c // 3)].add(x)
                    if bt(i + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(x)
                    cols[c].remove(x)
                    boards[(r // 3, c // 3)].remove(x)
            
            return False

        bt(0)