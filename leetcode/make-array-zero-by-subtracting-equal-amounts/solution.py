class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        nums.sort()

        i = 0
        res = 0
        while i < len(nums):
            if nums[i] != 0:
                sub = nums[i]
                for x in range(i, len(nums)):
                    nums[x] -= sub
                res += 1
            i += 1

        return res
