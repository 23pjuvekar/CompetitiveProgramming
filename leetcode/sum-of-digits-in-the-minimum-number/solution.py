class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        m = min(nums)

        res = 0
        while m > 0:
            res += m % 10
            m = m // 10
        
        return (res - 1) % 2
