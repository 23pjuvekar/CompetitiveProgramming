class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        res = 0
        if k > 0:
            res += min(k, numOnes)
            k -= numOnes
        if k > 0:
            k -= numZeros
        if k > 0:
            res -= min(k, numNegOnes)
            k -= numOnes
        
        return res
