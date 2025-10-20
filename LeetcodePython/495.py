class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        start = 0
        res = 0
        for t in timeSeries:
            if start > t:
                res += duration - (start - t)
            else:
                res += duration
            start = t + duration
        
        return res