class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        d = []
        for r in rectangles:
            d.append(min(r))

        m = 0
        res = 0
        for k, v in Counter(d).items():
            if k > m:
                m = k
                res = v
        return res
