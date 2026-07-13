class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        if not nums:
            return -1

        l = -1
        l_i = -1
        l_2 = -1
        
        for index, n in enumerate(nums):
            if n > l:
                l_2 = l
                l = n
                l_i = index
            elif n > l_2:
                l_2 = n
        
        if l >= 2 * l_2:
            return l_i
        else:
            return -1
