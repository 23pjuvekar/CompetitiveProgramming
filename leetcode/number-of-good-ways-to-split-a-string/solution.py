class Solution:
    def numSplits(self, s: str) -> int:

        n = len(s)
        left_dp = [0] * n
        left_set = set()
        right_dp = [0] * n
        right_set = set()

        for i in range(len(s)):
            if s[i] in left_set:
                left_dp[i] = len(left_set)
            else:
                left_set.add(s[i])
                left_dp[i] = len(left_set)
                

        for i in range(len(s) - 1, -1, -1):
            if s[i] in right_set:
                right_dp[i] = len(right_set)
            else:
                right_set.add(s[i])
                right_dp[i] = len(right_set)
                

        print(right_dp)
        print(left_dp)
        res = 0
        for i in range(len(s) - 1):
            if left_dp[i] == right_dp[i + 1]:
                res += 1

        return res
