class Solution:
    def sumZero(self, n: int) -> List[int]:

        res = []

        if n % 2 == 1:
            res.append(0)
            n -= 1
        
        for i in range(n // 2):
            res.append(i + 1)
            res.append(-(i + 1))
        
        return res
