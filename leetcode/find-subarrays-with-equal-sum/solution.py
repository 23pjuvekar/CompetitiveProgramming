class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        values = set()

        l = 0
        total = 0
        for r in range(len(nums)):
            if r - l + 1 > 2:
                total -= nums[l]
                l += 1
            total += nums[r] 
            if total in values:
                return True
            if r - l + 1 == 2:
                values.add(total)
        return False
