class Solution(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return 0.5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1] - p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        res = 0

        for p1 in points:
            for p2 in points:
                for p3 in points:
                    res = max(res, area(p1, p2, p3))
        return res
