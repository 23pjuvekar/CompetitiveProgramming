class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            if nums[l] + nums[r] < k:
                res = max(res, nums[l] + nums[r])
                l += 1
            else:
                r -= 1
        if res == 0:
            return -1
        return res
