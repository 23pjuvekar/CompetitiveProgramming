class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        arr = []
        for i in range(len(capacity)):
            arr.append(capacity[i] - rocks[i])
        arr.sort()
        res = 0
        for a in arr:
            if additionalRocks - a >= 0:
                additionalRocks -= a
                res += 1
        return res
