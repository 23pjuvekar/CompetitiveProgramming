class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        print(C)

        def isMagicSquare(r, c):
            vals = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    vals.append(grid[i][j])

            if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return 0

            s1 = sum(grid[r][c:c+3])
            s2 = sum(grid[r+1][c:c+3])
            s3 = sum(grid[r+2][c:c+3])
            s4 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
            s5 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
            s6 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
            s7 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            s8 = grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]

            if s1 == s2 == s3 == s4 == s5 == s6 == s7 == s8 == 15:
                return 1
            return 0
        res = 0
        for r in range(R - 2):
            for c in range(C - 2):
                res += isMagicSquare(r, c)
        return res
