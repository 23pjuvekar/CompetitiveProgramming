class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0
        c = 0

        for num in nums:
            if num == 0:
                c = 0
            else:
                c += 1
                res = max(res, c)
        return res
