class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        res = 0
        n = len(fruits)
        for i in range(n):
            res += fruits[i][i]
        # Calculate optimal corner paths
        dp = {}
        def dfs_1(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            if r == n - 1 and c == n - 1:
                return 0
            if r == c or r < 0 or c < 0 or r == n or c == n:
                return float("-inf")
            dp[(r, c)] = fruits[r][c] + max(dfs_1(r + 1, c -1), dfs_1(r + 1, c), dfs_1(r + 1, c + 1))
            return dp[(r, c)]
        dp_2 = {}
        def dfs_2(r, c):
            if (r, c) in dp_2:
                return dp_2[(r, c)]
            if r == n - 1 and c == n - 1:
                return 0
            if r == c or r < 0 or c < 0 or r == n or c == n:
                return float("-inf")
            dp_2[(r, c)] = fruits[r][c] + max(dfs_2(r - 1, c + 1), dfs_2(r, c + 1), dfs_2(r + 1, c + 1))
            return dp_2[(r, c)]
        return dfs_1(0, n - 1) + res + dfs_2(n - 1, 0)
