class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        res = 0
        for key, val in Counter(nums).items():
            if val == 1:
                res += key
        return res
