class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        res = [[0] * len(colsum) for _ in range(2)]
        

        for c in range(len(colsum)):
            if colsum[c] == 2:
                res[0][c] = 1
                res[1][c] = 1
                upper -= 1
                lower -= 1
        
        for c in range(len(colsum)):
            if colsum[c] == 1 and upper:
                res[0][c] = 1
                upper -= 1
            elif colsum[c] == 1 and lower:
                res[1][c] = 1
                lower -= 1
            elif colsum[c] == 1:
                return []
        
        if upper != 0 or lower != 0:
            return []
        return res
