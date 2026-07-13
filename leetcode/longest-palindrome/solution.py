class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        res = 0

        for char, item in Counter(s).items():
            if res % 2 != 1 and item % 2 == 1:
                res += 1
            res += (item // 2) * 2
        return res
