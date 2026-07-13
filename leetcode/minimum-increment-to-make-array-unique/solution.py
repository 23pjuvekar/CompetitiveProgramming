class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        min_val_used = float("-inf")
        res = 0
        for num in nums:
            curr = max(num, min_val_used + 1)
            res += (curr - num)
            min_val_used = curr
        return res

        # 1, 1, 2, 2, 3, 7
        # res = 0, min_val = 1
        # res = 1, min_val = 2
