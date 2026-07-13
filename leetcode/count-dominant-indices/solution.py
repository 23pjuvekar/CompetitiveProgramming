class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        prefix = []
        for i in range(len(nums) - 1, -1, -1):
            prev = 0
            if prefix:
                prev = prefix[-1]
            prefix.append(nums[i] + prev)
        prefix = prefix[::-1]
        n = len(nums)
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > prefix[i + 1] / (n - i - 1):
                res += 1
        return res
