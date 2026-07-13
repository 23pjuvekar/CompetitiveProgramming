class Solution:
    def minimumSum(self, num: int) -> int:
        h = []
        s = str(num)
        for c in s:
            h.append(c)
        h.sort(reverse=True)
        return min(int(h[3] + h[2] + h[1]) + int(h[0]),  int(h[3] + h[0]) + int(h[2]+ h[1]))
