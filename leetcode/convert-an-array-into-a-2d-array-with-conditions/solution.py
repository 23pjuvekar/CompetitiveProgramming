class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        d = defaultdict(int)
        m = 0
        for num in nums:
            d[num] += 1
            m = max(m, d[num])
        
        res = [[] for _ in range(m)]
        
        for key, val in d.items():
            for i in range(val):
                res[i].append(key)
        return res
