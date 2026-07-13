class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Forwards dp solution

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            if dp[i]:
                for w in wordDict:
                    if (i + len(w) <= len(s)) and (s[i : i + len(w)] == w):
                        dp[i + len(w)] = True
        
        return dp[len(s)]
