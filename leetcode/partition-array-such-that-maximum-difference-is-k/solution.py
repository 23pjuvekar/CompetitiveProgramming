class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        last = nums[0]
        res = 1
        for num in nums:
            if num - last > k:
                last = num
                res += 1
        return res
