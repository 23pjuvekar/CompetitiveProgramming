class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        mods = [[], [], []]
        
        for n in nums:
            rem = n % 3
            mods[rem].append(n)
            mods[rem].sort(reverse=True)
            if len(mods[rem]) > 3:
                mods[rem].pop()
        
        max_sum = 0
        
        if len(mods[0]) >= 3:
            max_sum = max(max_sum, sum(mods[0]))
            
        if len(mods[1]) >= 3:
            max_sum = max(max_sum, sum(mods[1]))
            
        if len(mods[2]) >= 3:
            max_sum = max(max_sum, sum(mods[2]))
            
        if len(mods[0]) >= 1 and len(mods[1]) >= 1 and len(mods[2]) >= 1:
            max_sum = max(max_sum, mods[0][0] + mods[1][0] + mods[2][0])
            
        return max_sum
