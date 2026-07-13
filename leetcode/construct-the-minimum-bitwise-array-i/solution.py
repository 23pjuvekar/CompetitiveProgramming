class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        res = []
        for n in nums:
            done = False
            for i in range(1, n):
                if i | (i+1) == n:
                    res.append(i)
                    done = True
                    break
            if done == False:
                res.append(-1)
        return res
