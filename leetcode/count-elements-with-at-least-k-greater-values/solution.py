class Solution:
    def countElements(self, nums: List[int], k: int) -> int:

        if k == 0:
            return len(nums)

        nums.sort()
        n = len(nums)

        if k >= n:
            return 0

        target = nums[n - k]
        count = 0
        for x in nums:
            if x < target:
                count += 1
                
        return count
