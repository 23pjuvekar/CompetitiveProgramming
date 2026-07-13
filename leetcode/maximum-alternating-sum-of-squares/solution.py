class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        n = len(nums)
        positive = n // 2
        negative = n // 2
        if n % 2 == 1:
            positive += 1
        for i in range(n):
            nums[i] = nums[i] ** 2
        nums.sort(reverse=True)
        # print(nums[:positive], nums[positive:])
        return sum(nums[:positive]) - sum(nums[positive:])
        # print(nums)
