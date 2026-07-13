class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:

        maximumHeight.sort(reverse=True)
        max_h = float("inf")
        res = 0
        for height in maximumHeight:
            curr = min(height, max_h)
            if curr <= 0:
                return -1
            max_h = curr - 1
            res += curr
        return res
