class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        counts = []
        for s in strs:
            counts.append([s.count("0"), s.count("1")])

        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            mCnt, nCnt = counts[i]
            dp[(i, m, n)] = dfs(i + 1, m, n) 
            if mCnt <= m and nCnt <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)],
                    1 + dfs(i + 1, m - mCnt, n - nCnt)
                )
            return dp[(i, m, n)]

        return dfs(0, m, n)
