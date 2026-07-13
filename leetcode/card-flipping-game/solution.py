class Solution(object):
    def flipgame(self, fronts, backs):
        same = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])

        ans = float('inf')
        for x in fronts:
            if x not in same:
                ans = min(ans, x)
        for x in backs:
            if x not in same:
                ans = min(ans, x)

        if ans == float('inf'):
            return 0
        return ans
