class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        res = 0

        for num in nums:
            num.sort()

        for j in range(len(nums[0])):
            curr = 0
            for i in range(len(nums)):
                curr = max(curr, nums[i][j])
            res += curr
        return res
