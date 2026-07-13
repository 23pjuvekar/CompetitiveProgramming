class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = {} # height, index
        def dfs(height, index):
            if (height, index) in dp:
                return dp[(height, index)]
            if height == n - 1:
                return triangle[height][index]
            if 0 <= index < len(triangle[height]):
                dp[(height, index)] = triangle[height][index] + min(dfs(height + 1, index), dfs(height + 1, index + 1))
                return dp[(height, index)]
        return dfs(0, 0)
