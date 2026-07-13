class Solution:
    def perfectPairs(self, nums: list[int]) -> int:
        nums = sorted(abs(x) for x in nums)
        n = len(nums)
        ans = 0
        left = 0
        for right in range(n):
            while nums[right] > 2 * nums[left]:
                left += 1
            ans += right - left
        return ans
