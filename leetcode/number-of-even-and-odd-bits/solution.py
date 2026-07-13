class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        index = 0
        res = [0, 0]
        while n:
            bit = n % 2
            n = n // 2
            if bit == 1:
                if index % 2 == 0:
                    res[0] += 1
                else:
                    res[1] += 1
            index += 1
        return res
