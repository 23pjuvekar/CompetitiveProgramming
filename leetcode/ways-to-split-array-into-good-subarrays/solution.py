class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        if sum(nums) == 0:
            return 0

        zero_in_between = []
        res = 1

        for num in nums:
            if num == 1:
                zero_in_between.append(0)
            else:
                if len(zero_in_between) != 0:
                    zero_in_between[-1] += 1

        if zero_in_between:
            zero_in_between.pop()

        for item in zero_in_between:
            res *= (1 + item)
            res = res % (10**9 + 7)

        return res % (10**9 + 7)
