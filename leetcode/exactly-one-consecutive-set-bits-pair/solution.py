class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        
        n = bin(n)[2:]
        res = 0
        for i in range(1, len(n)):
            if n[i-1] == "1" and n[i] == n[i-1]:
                res += 1
        return res == 1
