class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        n = len(matrix)

        for r in range(n):
            for c in range(n):
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
        
        for i in range(n):
            if len(rows[i]) != n or len(cols[i]) != n:
                return False
        return True
