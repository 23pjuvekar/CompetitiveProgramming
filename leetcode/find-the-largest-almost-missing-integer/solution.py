class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        if len(nums) == k:
            return max(nums)

        cnt = defaultdict(int)
        n = len(nums)

        for i in range(n):
            cnt[nums[i]] += min(i + 1, k, n - i)
        
        res = -1
        for key, val in cnt.items():
            if val == 1:
                res = max(res, key)
        return res
