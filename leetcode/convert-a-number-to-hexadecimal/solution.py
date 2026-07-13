class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return '0'

        if num < 0:
            num = (1 << 32) + num
        
        hex_digits = '0123456789abcdef'

        res = ''

        while num > 0:
            d = num % 16
            temp = hex_digits[d]
            res = temp + res
            num //= 16
        
        return res
