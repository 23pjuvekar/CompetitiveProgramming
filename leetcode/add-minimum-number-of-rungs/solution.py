class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        prev = 0
        for i in range(len(rungs)):
            amt = rungs[i] - prev
            if amt > dist:
                res += (amt) // dist
                if amt % dist == 0:
                    res -= 1
            prev = rungs[i]
        return res
