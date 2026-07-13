class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.sort()
        verticalCuts.sort()
        diff_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        diff_v = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(len(horizontalCuts) - 1):
            diff_h = max(diff_h, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            diff_v = max(diff_v, verticalCuts[i + 1] - verticalCuts[i])
        print(diff_v, diff_h)
        return (diff_v * diff_h) % (10 ** 9 + 7)
