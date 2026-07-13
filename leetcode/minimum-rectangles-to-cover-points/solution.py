class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:

        val = set()
        for x, y in points:
            val.add(x)
        val_list = list(val)
        val_list.sort()
        converd = -1
        res = 0
        for c in val_list:
            if c > converd:
                res += 1
                converd = c + w
        return res
