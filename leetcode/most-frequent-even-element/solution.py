class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        e_count = {}

        for n in nums:
            if n % 2 == 0:
                e_count[n] = 1 + e_count.get(n, 0)

        if len(e_count) == 0:
            return -1
        
        m = 0
        for key, value in e_count.items():
            if value > m:
                m = value
                res_n = []
                res = res_n
            
            if value == m:
                res.append(key)
        
        res_f = float('inf')
        for n in res:
            if n < res_f:
                res_f = n
        
        return res_f
