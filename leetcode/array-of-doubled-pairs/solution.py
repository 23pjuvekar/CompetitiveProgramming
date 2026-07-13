class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        count = Counter(arr)
        arr.sort(key=abs)
        for x in arr:
            if count[x] == 0:
                continue
            
            target = 2 * x
            if count[target] > 0:
                count[x] -= 1
                count[target] -= 1
            else:
                return False
                
        return True
