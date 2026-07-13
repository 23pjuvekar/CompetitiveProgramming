class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        curr = 0
        res = 0
        for g in gain:
            curr += g
            res = max(res, curr)
        return res
