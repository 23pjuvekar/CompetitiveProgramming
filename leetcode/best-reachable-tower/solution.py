class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        """
        if radius == 0:
            return [-1, -1]
        """

        best = -1
        res = [-1, -1]
        for x, y, q in towers:
            if abs(center[0] - x) + abs(center[1] - y) <= radius:
                if best < q:
                    best = q
                    res = [x, y]
                elif best == q:
                    res = min(res, [x, y])
        return res
