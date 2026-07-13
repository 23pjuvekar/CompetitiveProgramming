class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        stack = []

        for num in nums[::-1]:
            if not stack:
                stack.append(num)
            elif stack[-1] >= num:
                val = stack.pop()
                stack.append(val + num)
            else:
                stack.append(num)
        return max(stack)
