class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        """
        [1,1,2,3,   3  ,4,4,8,8]

        [3,3,7,  7  ,10,11,11]

        odd_first_index --> m + 1
        
        [10,11,11]

        even_first_index = m - 1

        """
        l = 0
        r = len(nums) - 1
        

        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        return nums[l]
