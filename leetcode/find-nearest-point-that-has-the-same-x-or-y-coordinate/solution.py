class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = float("inf")
        res = -1
        for i in range(len(points)):
            x2, y2 = points[i]
            if x != x2 and y != y2:
                continue
            else:
                if dis > abs(x - x2) + abs(y - y2):
                    res = i
                    dis = abs(x - x2) + abs(y - y2)
        return res
