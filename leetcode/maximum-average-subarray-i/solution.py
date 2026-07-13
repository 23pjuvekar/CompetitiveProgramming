class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        total = 0
        res = float("-inf")
        for r in range(len(nums)):
            total += nums[r]
            if r - l + 1 > k:
                total -= nums[l]
                l += 1
            if r - l + 1 == k:
                res = max(res, total / k)
        return res
