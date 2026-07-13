class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        prev_score = -1
        n = len(nums)
        if n % 2 == 1:
            n -= 1
        res = 0
        for i in range(0, n, 2):
            if prev_score == -1:
                prev_score = nums[i] + nums[i + 1]
            if prev_score != nums[i] + nums[i + 1]:
                return res
            res += 1
        return res
