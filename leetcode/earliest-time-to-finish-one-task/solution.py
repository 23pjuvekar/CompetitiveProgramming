class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:

        res = float("inf")

        for x, y in tasks:
            res = min(res, x + y)
        return res
