class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        teams = set()
        dp = defaultdict(int)
        for w, l in matches:
            teams.add(w)
            teams.add(l)
            dp[l] += 1
        res = [[], []]
        for i in teams:
            if dp[i] == 0:
                res[0].append(i)
            elif dp[i] == 1:
                res[1].append(i)
        res[0].sort()
        res[1].sort()
        return res
