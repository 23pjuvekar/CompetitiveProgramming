class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        memo = {}

        def dfs(r, c):
            if c < 0 or c >= n:
                return float('inf')
            
            if r == n - 1:
                return matrix[r][c]
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = matrix[r][c] + min(
                dfs(r + 1, c - 1), 
                dfs(r + 1, c), 
                dfs(r + 1, c + 1)
            )
            
            memo[(r, c)] = res
            return res

        return min(dfs(0, i) for i in range(n))
