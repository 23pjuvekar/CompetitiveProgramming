class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        f_big = 0
        s_big = 0

        for num in nums:
            if num > f_big:
                s_big = f_big
                f_big = num
            else:
                s_big = max(s_big, num)

        return (f_big - 1) * (s_big - 1)
