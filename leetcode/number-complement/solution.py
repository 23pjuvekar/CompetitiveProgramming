class Solution:
    def findComplement(self, num: int) -> int:
        
        l = 0
        x = num

        while x:
            x = x >> 1
            l += 1
        
        return num ^ ((2 ** l) - 1)
