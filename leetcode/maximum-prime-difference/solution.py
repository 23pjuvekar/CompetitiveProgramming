class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        pos = []
        for i, x in enumerate(nums): 
            if x >= 2: 
                for p in range(2, isqrt(x)+1): 
                    if x % p == 0: break 
                else: pos.append(i)
        return pos[-1] - pos[0]
