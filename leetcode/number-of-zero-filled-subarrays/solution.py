class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                if nums[l] == 0:
                    res += ((r - l) * (r - l + 1)) // 2
                l = r
        if nums[l] == 0:
            res += ((r - l + 2) * (r - l + 1)) // 2
        return res
