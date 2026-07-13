class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:

        ROW = len(grid)
        COL = len(grid[0])
        answer = [[0]*COL for _ in range(ROW)]
        
        diagonal = defaultdict(set)
    
        for i in range(ROW):
            for j in range(COL):
                
                answer[i][j] = len(diagonal[i-j])
                diagonal[i-j].add(grid[i][j])

        diagonal = defaultdict(set)

        for i in range(ROW-1, -1, -1):
            for j in range(COL-1, -1,-1):
                right = len(diagonal[i-j])
                diagonal[i-j].add(grid[i][j])
                answer[i][j] = abs(answer[i][j]-right)
        return answer
