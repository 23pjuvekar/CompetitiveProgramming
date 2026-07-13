class Solution:
    def minimumSteps(self, s: str) -> int:

        res = 0
        white = 0
        for i in range(len(s)):
            c = s[i]
            if c == "0":
                res += (i - white)
                white += 1
        
        return res
