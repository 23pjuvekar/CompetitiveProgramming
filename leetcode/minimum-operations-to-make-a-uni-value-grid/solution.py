class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        for row in grid:
            for n in row:
                if n % x != grid[0][0] % x:
                    return -1
        
        nums = [n for row in grid for n in row]
        nums.sort()

        prefix = 0
        total = sum(nums)
        res = float("inf")

        for i in range(len(nums)):
            c_l = nums[i] * i - prefix
            c_r = total - prefix - (nums[i] * (len(nums) - i))
            op = (c_l + c_r) // x
            res = min(res, op)
            prefix += nums[i]
        return res
