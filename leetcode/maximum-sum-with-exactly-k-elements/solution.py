class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        m = max(nums)

        res = 0
        for i in range(k):
            res += m
            m += 1
        return res
