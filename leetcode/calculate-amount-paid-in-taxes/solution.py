class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        start = 0
        res = 0

        for end, amt in brackets:
            end_p = min(end, income)
            res += (end_p - start) * (amt / 100)
            start = end_p
            if income < end:
                break
        return res
