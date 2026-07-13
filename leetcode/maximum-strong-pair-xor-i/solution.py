class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    res = max(res, nums[i] ^ nums[j])
        
        return res
