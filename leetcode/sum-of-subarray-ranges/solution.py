class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        res = 0
        for i in range(len(nums)):
            mn = nums[i]
            mx = nums[i]
            for j in range(i, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                res += (mx - mn)
        return res
