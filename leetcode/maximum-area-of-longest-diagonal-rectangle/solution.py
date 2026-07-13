class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        m = -1
        res = -1

        for d in dimensions:
            if (d[0] * d[0] + d[1] * d[1]) ** 0.5 > m:
                m = (d[0] * d[0] + d[1] * d[1]) ** 0.5
                res = d[0] * d[1]
            elif (d[0] * d[0] + d[1] * d[1]) ** 0.5 == m:
                res = max(res, d[0] * d[1])
        return res
