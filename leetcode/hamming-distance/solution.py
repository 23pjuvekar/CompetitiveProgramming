class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        res = 0

        while x or y:
            digit_1 = x % 2
            digit_2 = y % 2
            x = x // 2
            y = y // 2
            if digit_1 != digit_2:
                res += 1
        
        return res
