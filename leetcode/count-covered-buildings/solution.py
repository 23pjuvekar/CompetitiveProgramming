class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        row_min = defaultdict(lambda: float('inf'))
        row_max = defaultdict(lambda: float('-inf'))
        col_min = defaultdict(lambda: float('inf'))
        col_max = defaultdict(lambda: float('-inf'))
        for r, c in buildings:
            row_min[r] = min(row_min[r], c)
            row_max[r] = max(row_max[r], c)
            col_min[c] = min(col_min[c], r)
            col_max[c] = max(col_max[c], r)
            
        res = 0
        for r, c in buildings:
            if (row_min[r] < c and row_max[r] > c and 
                col_min[c] < r and col_max[c] > r):
                res += 1
                
        return res
