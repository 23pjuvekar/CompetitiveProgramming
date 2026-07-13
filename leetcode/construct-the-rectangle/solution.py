class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        res = [1, area]
        for w in range(1, int(area ** 0.5) + 1):
            if area % w == 0:
                l = area // w
                res = [l, w]
        return res
