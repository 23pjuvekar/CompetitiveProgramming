class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        res = []
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return False
            if res and res[-1] == (nums[i + 1] - nums[i]) / abs(nums[i + 1] - nums[i]):
                continue
            res.append((nums[i + 1] - nums[i]) / abs(nums[i + 1] - nums[i]))
        return res == [1, -1, 1]
