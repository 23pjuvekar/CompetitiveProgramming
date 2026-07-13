class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:

        n = len(nums)
        right_min = [0] * n
        right_min[-1] = nums[-1]
        for i in range(n - 2, 0, -1):
            right_min[i] = min(right_min[i + 1], nums[i])

        res = 0
        left_max = nums[0]
        
        for i in range(1, n - 1):
            if left_max < nums[i] < right_min[i + 1]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
            left_max = max(left_max, nums[i])
            
        return res
