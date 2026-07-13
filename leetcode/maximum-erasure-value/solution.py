class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        curr_window = set()
        l = 0
        total = 0
        res = 0
        for r in range(len(nums)):
            while nums[r] in curr_window:
                curr_window.remove(nums[l])
                total -= nums[l]
                l += 1
            curr_window.add(nums[r])
            total += nums[r]
            res = max(res, total)
        return res
