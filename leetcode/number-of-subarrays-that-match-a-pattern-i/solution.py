class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        

        dp = []

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                dp.append(1)
            elif nums[i] - nums[i - 1] < 0:
                dp.append(-1)
            else:
                dp.append(0)

        n = len(pattern)
        res = 0
        for i in range(len(dp) - n + 1):
            if dp[i:i+n] == pattern:
                res += 1
        return res
