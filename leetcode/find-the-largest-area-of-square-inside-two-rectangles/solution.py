class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        res = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i + 1, n):
                x_b, y_b = max(bottomLeft[i][0], bottomLeft[j][0]), max(bottomLeft[i][1], bottomLeft[j][1])
                x_t, y_t = min(topRight[i][0], topRight[j][0]), min(topRight[i][1], topRight[j][1])
                w = max(x_t - x_b, 0)
                h = max(y_t - y_b, 0)
                res = max(res, min(w, h) ** 2)
        return res
