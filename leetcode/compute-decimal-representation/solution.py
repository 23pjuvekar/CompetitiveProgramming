class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        res = []
        curr_offset = 1
        while n:
            if n % 10 != 0:
                res.append(curr_offset * (n % 10))
            curr_offset *= 10
            n = n // 10
        return res[::-1]
