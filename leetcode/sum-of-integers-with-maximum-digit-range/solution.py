class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def digit_range(value):
            digits = [int(d) for d in str(value)]
            return max(digits) - min(digits)

        max_range = max(digit_range(num) for num in nums)
        return sum(num for num in nums if digit_range(num) == max_range)
