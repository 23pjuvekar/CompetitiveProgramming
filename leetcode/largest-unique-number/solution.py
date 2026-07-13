class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        res = -1
        for key, val in Counter(nums).items():
            if val == 1:
                res = max(res, key)
        return res
