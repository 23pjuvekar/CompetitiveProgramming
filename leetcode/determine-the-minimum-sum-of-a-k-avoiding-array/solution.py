class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = []
        for i in range(1, min((k // 2) + 1, n + 1)):
            res.append(i)
        curr = k 
        while len(res) < n:
            res.append(curr)
            curr += 1
        return sum(res)
