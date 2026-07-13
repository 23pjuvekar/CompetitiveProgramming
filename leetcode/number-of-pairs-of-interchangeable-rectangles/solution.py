class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        ratios = defaultdict(int)
        for w, h in rectangles:
            ratios[w / h] += 1
        res = 0
        for key, val in ratios.items():
            res += (val) * (val - 1) // 2
        return res
