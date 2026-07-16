class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        key_counts = defaultdict(int)
        good_pairs = 0
        for index in range(n):
            key = nums[index] - index
            good_pairs += key_counts[key]
            key_counts[key] += 1
        return total_pairs - good_pairs
