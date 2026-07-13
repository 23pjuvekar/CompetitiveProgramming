class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        r1, r2 = toBeRemoved
        result = []
        for start, end in intervals:
            if end <= r1 or start >= r2:
                result.append([start, end])
            else:
                if start < r1 < end:
                    result.append([start, r1])
                if start < r2 < end:
                    result.append([r2, end])
                    
        return result
