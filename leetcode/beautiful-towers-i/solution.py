class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:

        n = len(heights)
        max_total = 0
        for i in range(n):
            current_sum = heights[i]
            last_h = heights[i]
            for j in range(i - 1, -1, -1):
                last_h = min(last_h, heights[j])
                current_sum += last_h
            last_h = heights[i]
            for j in range(i + 1, n):
                last_h = min(last_h, heights[j])
                current_sum += last_h
            max_total = max(max_total, current_sum)
            
        return max_total
