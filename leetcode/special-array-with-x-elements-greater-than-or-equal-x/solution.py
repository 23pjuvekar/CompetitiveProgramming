class Solution:
    def specialArray(self, nums: List[int]) -> int:

        if 0 not in nums:
            nums.append(0)
        nums.sort()
        seen = set()
        n = len(nums)

        for i in range(1, len(nums)):
            if nums[i] in seen:
                continue
            if nums[i - 1] < n - i <= nums[i]:
                return n - i
            seen.add(nums[i])
        return -1
