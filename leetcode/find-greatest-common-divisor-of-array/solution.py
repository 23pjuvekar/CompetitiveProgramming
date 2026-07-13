class Solution:
    def findGCD(self, nums: List[int]) -> int:

        minimum = min(nums)
        maximum = max(nums)
        res = 1

        for i in range(1, minimum + 1):
            if maximum % i == 0 and minimum % i == 0:
                res = i
        return res
