class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        l = 0
        double = -1
        res = 1

        for r in range(1, len(s)):
            if s[r-1] == s[r]:
                if double == -1:
                    double = r
                else:
                    l = double
                    double = r 
            
            res = max(res, r - l + 1)
        
        return res
