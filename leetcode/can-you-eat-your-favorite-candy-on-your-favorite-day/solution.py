class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:

        pre_sum = [0] * len(candiesCount)
        for i in range(1, len(candiesCount)):
            pre_sum[i] = pre_sum[i - 1] + candiesCount[i - 1]
        res = []
        for ft, fd, dc in queries:
            res.append((fd + 1) * dc > pre_sum[ft] and pre_sum[ft] + candiesCount[ft] >= fd + 1)
        return res
