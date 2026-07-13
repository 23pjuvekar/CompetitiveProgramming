class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
        one_i = -1
        n_i = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                one_i = i
            elif nums[i] == n:
                n_i = i
        res = 0
        if one_i > n_i:
            res -= 1
        
        res += one_i
        res += (n - n_i - 1)
        return res
