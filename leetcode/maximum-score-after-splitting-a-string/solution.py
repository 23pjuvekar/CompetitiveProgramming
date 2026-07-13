class Solution:
    def maxScore(self, s: str) -> int:

        ones = s.count('1')
        zeros = 0
        res = 0

        for i in range(len(s) - 1):
            zeros += s[i] == '0'
            ones -= s[i] == '1'
            res = max(res, zeros + ones)
        
        return res
