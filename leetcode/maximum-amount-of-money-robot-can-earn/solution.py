class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        ROWS, COLS = len(coins), len(coins[0])
        dp = {}
        def dfs(r, c, nut):
            if r >= ROWS or c >= COLS:
                return float('-inf')
            if r == ROWS - 1 and c == COLS - 1:
                val = coins[r][c]
                if val < 0 and nut > 0:
                    return 0
                return val
            if (r, c, nut) in dp:
                return dp[(r, c, nut)]
            val = coins[r][c]
            if val >= 0:
                down = dfs(r + 1, c, nut)
                right = dfs(r, c + 1, nut)
                best = max(down, right) + val
            else:
                skip = float('-inf')
                if nut > 0:
                    skip_down = dfs(r + 1, c, nut - 1)
                    skip_right = dfs(r, c + 1, nut - 1)
                    skip = max(skip_down, skip_right)
                take_down = dfs(r + 1, c, nut) + val
                take_right = dfs(r, c + 1, nut) + val
                best = max(skip, take_down, take_right)
            dp[(r, c, nut)] = best
            return best
        return dfs(0, 0, 2)
