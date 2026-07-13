class Solution:
    def minOperations(self, nums: List[int]) -> int:

        amt = 0
        m = 0
        for num in nums:
            curr = 0
            while num:
                if num % 2 == 1:
                    num -= 1
                    amt += 1
                else:
                    num = num // 2
                    curr += 1
                    m = max(m, curr)
        return amt + m
