class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = (10 ** 9) + 7
        n = len(nums)
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0] = 1
        prefix[0] = 1
        max_d = deque()
        min_d = deque()
        L = 0
        for r in range(n):
            x = nums[r]
            while max_d and max_d[-1] < x:
                max_d.pop()
            max_d.append(x)
            while min_d and min_d[-1] > x:
                min_d.pop()
            min_d.append(x)
            while max_d and min_d and max_d[0] - min_d[0] > k:
                if nums[L] == max_d[0]:
                    max_d.popleft()
                if nums[L] == min_d[0]:
                    min_d.popleft()
                L += 1
            ways = prefix[r]
            if L > 0:
                ways = (ways - prefix[L - 1]) % MOD
            dp[r + 1] = ways
            prefix[r + 1] = (prefix[r] + ways) % MOD
        return dp[n]
