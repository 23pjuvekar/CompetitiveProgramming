class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        nums.sort()
        l = 0
        res = 0
        n = len(nums)
        for r in range(len(nums)):
            while nums[l] * k < nums[r]:
                l += 1
            res = max(res, r - l + 1)
        return n - res
