class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        l, r = bounds[0]

        for i in range(1, len(original)):
            diff = original[i] - original[i - 1]
            
            l = max(l + diff, bounds[i][0])
            r = min(r + diff, bounds[i][1])

            if l > r:
                return 0
        
        return r - l + 1
