class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        at = []
        for d, s in zip(dist, speed):
            at.append(math.ceil(d / s))
        at.sort()
        for t in range(len(at)):
            if at[t] <= t:
                return t
        return len(at)
