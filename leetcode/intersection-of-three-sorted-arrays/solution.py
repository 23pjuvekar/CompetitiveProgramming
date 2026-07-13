class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        c1 = set(arr1)
        c2 = set(arr2)
        res = []
        for num in arr3:
            if num in c1 and num in c2:
                res.append(num)
        return res
