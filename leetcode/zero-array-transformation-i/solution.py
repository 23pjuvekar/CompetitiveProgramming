class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        dp = [0] * (len(nums) + 1)

        for querie in queries:
            dp[querie[0]] += 1
            dp[querie[1] + 1] -= 1

        for index in range(len(dp) - 1):
            if index == 0:
                if dp[index] < nums[index]:
                    return False
            else:    
                dp[index] = dp[index - 1] + dp[index]
                if dp[index] < nums[index]:
                    return False
        return True
