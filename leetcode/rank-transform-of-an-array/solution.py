class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        unique = list(set(arr))
        unique.sort()
        map_key = {}
        for i in range(len(unique)):
            map_key[unique[i]] = i+1
        
        res = []
        for num in arr:
            res.append(map_key[num])
        
        return res
