class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        last = 0
        res = 1
        curr = 0

        for i in range(len(nums) - 1):
            if nums[i] - nums[i + 1] > 0:
                if last == 1:
                    curr += 1
                    res = max(res, curr)
                else:
                    last = 1
                    curr = 2
                    res = max(res, curr)
            elif nums[i] - nums[i + 1] < 0:
                if last == -1:
                    curr += 1
                    res = max(res, curr)
                else:
                    last = -1
                    curr = 2
                    res = max(res, curr)
            else:
                last = 0
                curr = 0
        return res
