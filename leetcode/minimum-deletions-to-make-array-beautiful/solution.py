class Solution:
    def minDeletion(self, nums: List[int]) -> int:

        i = 0 
        stack = []
        res = 0

        while i < len(nums):
            if len(stack) % 2 == 0:
                stack.append(nums[i])
            else:
                if stack[-1] != nums[i]:
                    stack.append(nums[i])
                else:
                    res += 1

            i += 1

        if len(stack) % 2 == 1:
            res += 1
        return res
