class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        MOD = 10**9 + 7
        total_sum = sum(arr)
        
        def kadane(nums):
            max_so_far = 0
            curr_max = 0
            for x in nums:
                curr_max = max(0, curr_max + x)
                max_so_far = max(max_so_far, curr_max)
            return max_so_far

        if k == 1:
            return kadane(arr) % MOD
        
        max_two_copies = kadane(arr + arr)
        
        if total_sum > 0:
            return (max_two_copies + (k - 2) * total_sum) % MOD
        else:
            return max_two_copies % MOD
