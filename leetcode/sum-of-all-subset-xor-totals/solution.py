class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def bt(i, total):
            res[0] += total ^ nums[i]
            if i + 1 < len(nums):
                bt(i+1, total)
                bt(i+1, total ^ nums[i])

        res = [0]
        if len(nums) == 0:
            return 0
        bt(0, 0)
        return res[0]
