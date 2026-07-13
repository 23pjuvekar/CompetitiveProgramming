class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        nums.sort(reverse=True)
        return nums[0] * nums[1] * (10 ** 5)
