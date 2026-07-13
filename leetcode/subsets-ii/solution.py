from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            # Include the current number
            curr.append(nums[i])
            dfs(i + 1)

            # Exclude the current number and avoid duplicates
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return res
