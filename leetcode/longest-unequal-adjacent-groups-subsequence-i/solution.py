class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        dp = [0, 1]
        res = [[], []]

        for w, g in zip(words, groups):
            if g == dp[0]:
                res[0].append(w)
                if g == 1:
                    dp[0] = 0
                else:
                    dp[0] = 1
            if g == dp[1]:
                res[1].append(w)
                if g == 1:
                    dp[1] = 0
                else:
                    dp[1] = 1
        if len(res[0]) > len(res[1]):
            return res[0]
        return res[1]
