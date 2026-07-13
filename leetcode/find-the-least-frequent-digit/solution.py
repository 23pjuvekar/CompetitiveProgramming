class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        res = ""
        min_amt = float('inf')
        for key, val in Counter(str(n)).items():
            if val < min_amt:
                res = key
                min_amt = val
            elif val == min_amt:
                res = min(res, key)
        return int(res)
