class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:

        last_one = -float("inf")
        last_two = -float("inf")
        res = float("inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                last_one = i
            elif nums[i] == 2:
                last_two = i
            res = min(res, abs(last_two - last_one))
        if res == float("inf"):
            return -1
        return res
