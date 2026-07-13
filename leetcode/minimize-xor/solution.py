class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        def count_bits(n):
            res = 0
            while n > 0:
                res += n & 1
                n = n >> 1
            return res
        
        c1 = count_bits(num1)
        c2 = count_bits(num2)
        x = num1
        i = 0

        while c1 > c2:
            if x & (1 << i):
                c1 -= 1
                x = x ^ (1 << i)
            i += 1
        
        while c1 < c2:
            if x & (1 << i) == 0:
                c1 += 1
                x = x | (1 << i)
            i += 1
        
        return x
