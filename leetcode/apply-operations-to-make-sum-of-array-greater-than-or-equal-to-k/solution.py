class Solution:
    def minOperations(self, k: int) -> int:
        
        res = k - 1
        for x in range(1, k + 1):
            res = min(res, (x - 1) + (ceil(k / x) - 1))
        return res
