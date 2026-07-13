class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:

        nums.append(float("inf"))
        nums.append(float("-inf"))
        nums.sort()
        res = []
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1] and nums[i] != nums[i - 1] and nums[i] + 1 != nums[i + 1] and nums[i] - 1 != nums[i - 1]:
                res.append(nums[i])
        return res
