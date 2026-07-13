class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:

        res = [float("-inf")] * len(nums)

        m = float("-inf")
        for i in range(len(nums)):
            if nums[i] > m:
                res[i] = nums[i]
            m = max(m, nums[i])
        
        m = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > m:
                res[i] = nums[i]
            m = max(m, nums[i])

        ans = []
        for num in res:
            if num != float("-inf"):
                ans.append(num)
        return ans
