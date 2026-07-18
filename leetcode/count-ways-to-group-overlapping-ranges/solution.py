class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        modulus = 10**9 + 7
        sorted_ranges = sorted(ranges)
        group_count = 0
        current_end = -1
        for start, end in sorted_ranges:
            if start > current_end:
                group_count += 1
            current_end = max(current_end, end)
        return pow(2, group_count, modulus)
