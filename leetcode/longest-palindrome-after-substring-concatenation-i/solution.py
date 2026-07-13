class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        res = 0
        n, m = len(s), len(t)
        
        for i in range(n):
            for j in range(i, n + 1):
                sub_s = s[i:j]
                
                for k in range(m):
                    for l in range(k, m + 1):
                        sub_t = t[k:l]
                        
                        combined = sub_s + sub_t
                        if combined == combined[::-1]:
                            res = max(res, len(combined))
        return res
