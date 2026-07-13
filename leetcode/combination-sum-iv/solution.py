class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        def bt(total):
            if total in memo:
                return memo[total]
            if total == target:
                return 1
            if total > target:
                return 0
            res = 0
            for num in nums:
                res += bt(total + num)
            memo[total] = res
            return res
            
        return bt(0)
