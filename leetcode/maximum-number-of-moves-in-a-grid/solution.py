class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        currentMoves = [0] * numRows
        maxMovesFound = 0

        for col in range(numCols - 1):
            nextMoves = [-1] * numRows
            for row in range(numRows):
                if currentMoves[row] == -1:
                    continue
                for rowOffset in (-1, 0, 1):
                    nextRow = row + rowOffset
                    if nextRow < 0 or nextRow >= numRows:
                        continue
                    if grid[nextRow][col + 1] > grid[row][col]:
                        candidateMoves = currentMoves[row] + 1
                        nextMoves[nextRow] = max(nextMoves[nextRow], candidateMoves)
                        maxMovesFound = max(maxMovesFound, candidateMoves)
            currentMoves = nextMoves

        return maxMovesFound
