class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        while len(nums) > 1:
            n = []
            for i in range(len(nums) - 1):
                n.append((nums[i] + nums[i + 1]) % 10)
            nums = n
        return nums[0]
