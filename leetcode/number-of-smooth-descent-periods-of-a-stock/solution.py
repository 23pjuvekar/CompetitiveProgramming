class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        l = 0
        res = 0
        for r in range(len(prices)):
            if r != 0 and prices[r] != prices[r - 1] - 1:  
                l = r
            res += (r - l + 1)
        return res
