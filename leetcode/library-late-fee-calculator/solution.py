class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        
        res = 0

        for amt in daysLate:
            if amt == 1:
                res += 1
            elif 2 <= amt <= 5:
                res += 2 * amt
            else:
                res += 3 * amt
        return res
