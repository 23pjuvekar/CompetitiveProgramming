class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []

        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                res[r][c] = original[r * n + c]
            
        return res
