class Solution:
    def findLucky(self, arr: List[int]) -> int:

        res = -1

        for item in Counter(arr).items():
            if item[0] == item[1]:
                res = max(res, item[0])
            
        return res
