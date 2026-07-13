class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        res = 0
        l = 0
        while l < n:
            if nums[l] % 2 != 0 or nums[l] > threshold:
                l += 1
                continue

            r = l
            while r + 1 < n and nums[r + 1] <= threshold and nums[r + 1] % 2 != nums[r] % 2:
                r += 1

            res = max(res, r - l + 1)
            l = r + 1
        return res
