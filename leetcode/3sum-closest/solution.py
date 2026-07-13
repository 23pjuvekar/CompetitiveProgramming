class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        res = float("inf")

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum
                
                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1

        return res
