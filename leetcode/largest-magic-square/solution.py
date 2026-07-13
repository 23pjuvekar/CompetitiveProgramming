class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])

        row_prefix = [[0] * C for _ in range(R)]
        for i in range(R):
            row_prefix[i][0] = grid[i][0]
            for j in range(1, C):
                row_prefix[i][j] = row_prefix[i][j - 1] + grid[i][j]

        col_prefix = [[0] * C for _ in range(R)]
        for j in range(C):
            col_prefix[0][j] = grid[0][j]
            for i in range(R):
                col_prefix[i][j] = grid[i][j] + col_prefix[i - 1][j]


        for edge in range(min(R, C), 1, - 1):
            for i in range(R - edge + 1):
                for j in range(C - edge + 1):
                    stdsum = row_prefix[i][j + edge - 1] - (0 if j == 0 else row_prefix[i][j - 1])
                    check = True
                    for ii in range(i + 1, i + edge):
                        if (row_prefix[ii][j + edge - 1] - (0 if j == 0 else row_prefix[ii][j - 1]) != stdsum):
                            check = False
                            break
                    if not check:
                        continue
                    
                    for jj in range(j, j + edge):
                        if (col_prefix[i + edge - 1][jj] - (0 if i == 0 else col_prefix[i - 1][jj]) != stdsum):
                            check = False
                            break
                    if not check:
                        continue

                    d1 = d2 = 0
                    for k in range(edge):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + edge - 1 - k]
                    if d1 == stdsum and d2 == stdsum:
                        return edge
        
        return 1
