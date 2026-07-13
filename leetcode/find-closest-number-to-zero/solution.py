class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        res = nums[0]
        for num in nums:
            if abs(num) < abs(res):
                res = num
            elif abs(num) == abs(res) and num > 0:
                res = num
        return res
