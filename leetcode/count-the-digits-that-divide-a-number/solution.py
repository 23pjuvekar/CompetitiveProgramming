class Solution:
    def countDigits(self, num: int) -> int:
        
        curr = num
        res = 0
        while curr:
            digit = curr % 10
            curr = curr // 10
            if num % digit == 0:
                res += 1
        return res
