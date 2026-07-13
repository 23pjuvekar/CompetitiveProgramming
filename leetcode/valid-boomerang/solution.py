class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        def slopeCalc(p1, p2):
            x, y = p1
            x2, y2 = p2
            if (x - x2) == 0:
                return float("inf")
            return (y - y2) / (x - x2)

        return slopeCalc(points[0], points[1]) != slopeCalc(points[1], points[2]) and points[0] != points[1] != points[2]
