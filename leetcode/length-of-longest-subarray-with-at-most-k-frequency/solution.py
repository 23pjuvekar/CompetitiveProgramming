class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        mp = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(nums)):
            mp[nums[r]] += 1
            while mp[nums[r]] > k:
                mp[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
