class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        current_sum = 0
        ans = -1
        for i in range(len(nums)):
            if current_sum > nums[i]:
                ans = current_sum + nums[i]
            current_sum += nums[i]
        return ans
