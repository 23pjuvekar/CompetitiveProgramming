class Solution:
    def minLength(self, nums: List[int], k: int) -> int:

        l = 0
        total = 0
        count = defaultdict(int)
        res = float("inf")
        for r in range(len(nums)):
            count[nums[r]] += 1
            if count[nums[r]] == 1:
                total += nums[r]
            while total >= k:
                res = min(res, r - l + 1)
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    total -= nums[l]
                l += 1
        if res == float("inf"):
            return -1
        return res
