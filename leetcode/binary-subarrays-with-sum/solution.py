class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count_seen = defaultdict(int)
        count_seen[0] += 1
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count_seen:
                res += count_seen[curr_sum - goal]
            count_seen[curr_sum] += 1
        return res
