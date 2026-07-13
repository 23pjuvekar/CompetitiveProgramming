class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = 0
        p1 = -1
        p2 = -1
        for x, y in intervals:
            if p2 < x:
                res += 2
                p1, p2 = y - 1, y
            elif p1 < x:
                res += 1
                p1, p2 = p2, y
        return res
