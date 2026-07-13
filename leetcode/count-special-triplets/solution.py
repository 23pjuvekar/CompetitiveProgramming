class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        num_right = Counter(nums)
        num_left = defaultdict(int)
        ans = 0
        for v in nums:
            target = v * 2
            l_cnt = num_left[target]
            num_left[v] += 1
            num_right[v] -= 1
            r_cnt = num_right[target]
            ans = (ans + l_cnt * r_cnt) % MOD

        return ans
