class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        best = values[0] - 1
        res = 0
        for i in range(1, len(values)):
            res = max(res, best + values[i])
            best = max(best - 1, values[i] - 1)
        return res
