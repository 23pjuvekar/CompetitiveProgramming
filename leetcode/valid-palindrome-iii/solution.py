class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        memo = {}
        def lps(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == s[j]:
                res = 2 + lps(i + 1, j - 1)
            else:
                res = max(lps(i + 1, j), lps(i, j - 1))
            
            memo[(i, j)] = res
            return res

        return (len(s) - lps(0, len(s) - 1)) <= k
