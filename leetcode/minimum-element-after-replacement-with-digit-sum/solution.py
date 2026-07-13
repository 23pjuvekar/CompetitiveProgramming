class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float("inf")
        for i in range(len(nums)):
            num = nums[i]
            sum_val = 0
            for c in str(num):
                sum_val += int(c)
            nums[i] = sum_val
            res = min(res, sum_val)
        return res
