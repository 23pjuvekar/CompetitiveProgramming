class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        tracker = []
        count = 0

        for n in nums:
            if n == 1:
                count += 1
            else:
                tracker.append(count)
                count = 0

        tracker.append(count)

        if len(tracker) == 1:
            return len(nums) - 1

        res = 0
        for i in range(len(tracker) - 1):
            res = max(res, tracker[i] + tracker[i + 1])

        return res
