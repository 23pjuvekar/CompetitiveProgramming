class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x, y = points[0]
        for xp, yp in points:
            res += max(abs(xp-x), abs(yp-y))
            x, y = xp, yp
        return res
