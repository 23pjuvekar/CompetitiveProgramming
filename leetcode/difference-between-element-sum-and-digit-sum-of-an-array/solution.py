class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        e_sum = 0
        d_sum = 0
        for num in nums:
            e_sum += num
            for c in str(num):
                d_sum += int(c)
        return e_sum - d_sum
