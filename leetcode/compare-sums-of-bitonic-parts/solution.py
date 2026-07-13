class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:

        peak_idx = 0
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                peak_idx = i
                break
        asc_sum = sum(nums[:peak_idx + 1])
        desc_sum = sum(nums[peak_idx:])
        if asc_sum > desc_sum:
            return 0
        elif desc_sum > asc_sum:
            return 1
        else:
            return -1
