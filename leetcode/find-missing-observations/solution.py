class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)
        res = [1] * n
        total = mean * (m + n)
        total -= sum(rolls)
        if total < n or total > n * 6:
            return []
        total -= n
        i = 0
        while total > 0:
            res[i] += min(total, 5) 
            total -= min(total, 5)
            i += 1
        return res
