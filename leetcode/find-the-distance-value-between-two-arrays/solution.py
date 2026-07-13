class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        

        vals = set(arr2)
        res = 0
        for num in arr1:
            good = True
            for i in range(num - d, num + d + 1):
                if i in vals:
                    good = False
                    break
            if good:
                res += 1
        return res
