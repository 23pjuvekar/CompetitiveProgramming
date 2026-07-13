class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for index, num in enumerate(nums):
            if num > 0:
                break
            
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            
            l = index + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + nums[index]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[index], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        return res
