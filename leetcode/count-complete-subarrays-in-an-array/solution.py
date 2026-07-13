class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        N = len(set(nums))
        M = len(nums)
        mp = defaultdict(int)
        res = 0
        l = 0
        for i in range(len(nums)):
            n = nums[i]
            mp[n] += 1
            while len(mp) == N:
                res += (M - i)
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                l += 1
        return res
