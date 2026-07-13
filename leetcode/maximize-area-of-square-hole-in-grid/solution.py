class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        res_v = 1
        res_h = 1
        curr = 1
        hBars.sort()
        vBars.sort()
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                curr += 1
                res_h = max(curr, res_h)
            else:
                curr = 1
        curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                curr += 1
                res_v = max(curr, res_v)
            else:
                curr = 1
        return min(res_v + 1, res_h + 1) ** 2
