class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num) - 1
        res = -1
        
        for i in range(n, -1, -1):
            if int(num[i]) % 2 != 0:
                res = i
                break
        
        return "" if res == -1 else num[:i + 1]
