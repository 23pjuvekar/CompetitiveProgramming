class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            start = i + k
            end = i - k
            good = True
            if 0 <= start < n and nums[start] >= nums[i]:
                good = False
            if 0 <= end < n and nums[end] >= nums[i]:
                good = False
            if good:
                res += nums[i]
        return res
