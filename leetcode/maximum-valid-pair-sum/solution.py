class Solution:
    def maxValidPairSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i + 1])

        best = 0
        for i in range(n - k):
            best = max(best, nums[i] + suffix_max[i + k])
        return best
