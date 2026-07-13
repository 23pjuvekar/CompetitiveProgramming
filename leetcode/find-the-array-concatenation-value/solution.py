class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            res += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            res += nums[l]
        return res
