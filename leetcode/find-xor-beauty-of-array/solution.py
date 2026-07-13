class Solution:
    def xorBeauty(self, nums: List[int]) -> int:

        curr = 0
        for i in range(len(nums)):
            curr = nums[i] ^ curr
        return curr
