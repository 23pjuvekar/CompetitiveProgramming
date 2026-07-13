class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        l = 0
        window_sum = 0

        for r in range(len(nums)):
            if (r - l + 1) > (2*k + 1):
                window_sum -= nums[l]
                l += 1
            window_sum += nums[r]
            if (r - l + 1) == (2*k + 1):
                res[l + k] = window_sum // ((2*k + 1))
        return res
