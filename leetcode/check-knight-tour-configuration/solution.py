class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        if grid[0][0] != 0:
            return False

        valid_moves = [
                [-1, -2],
                [-1, 2],
                [1, -2],
                [1, 2],
                [-2, 1],
                [-2, -1],
                [2, 1],
                [2, -1]
            ]

        moves_in_order = [] # [move number, row, column]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                moves_in_order.append([grid[r][c], r, c])
        moves_in_order.sort()
        last_row, last_column = moves_in_order[0][1:]
        for _, row, column in moves_in_order[1:]:
            if [row - last_row, column - last_column] not in valid_moves:
                return False
            last_row = row
            last_column = column
        return True
