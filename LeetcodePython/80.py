class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        """

        [1,1,1,2,2,3]

        [1,1,2,2,3]

        """
        
        insert_index = 0
        for i in range(len(nums)):
            if 0 <= insert_index - 1 and 0 <= insert_index - 2 and nums[i] == nums[insert_index - 1] == nums[insert_index - 2]:
                continue
            else:
                nums[insert_index] = nums[i]
                insert_index += 1
        return insert_index