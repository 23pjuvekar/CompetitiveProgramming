class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        res = 0
        for key, val in Counter(nums).items():
            res += ((val - 1) * val) // 2
        return res
