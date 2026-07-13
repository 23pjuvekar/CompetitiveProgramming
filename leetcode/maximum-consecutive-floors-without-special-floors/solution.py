class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:

        bottom -= 1 
        top += 1
        special.append(bottom)
        special.append(top)
        special.sort()
        res = 0
        for i in range(len(special) - 1):
            res = max(res, special[i + 1] - special[i] - 1)
        return res
