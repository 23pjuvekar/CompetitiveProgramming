class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_beauty = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            window_size = right - left + 1
            if window_size > max_beauty:
                max_beauty = window_size

        return max_beauty
