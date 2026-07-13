class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        def increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return 0
            return 1

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                new_array = nums[:i] + nums[j:]
                res += increasing(new_array)
        return res
