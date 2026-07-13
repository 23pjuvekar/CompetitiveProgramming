class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        # optimal
        element_counts = Counter(nums)
        unique_sorted_elements = sorted(list(set(nums)))
        max_covered_value = float("-inf")
        total_distinct_elements = 0
        for current_element in unique_sorted_elements:
            element_frequency = element_counts[current_element]
            effective_interval_start = max(current_element - k, max_covered_value)
            effective_interval_end = current_element + k
            num_newly_covered_elements = min(effective_interval_end - effective_interval_start + 1, element_frequency)
            total_distinct_elements += max(0, num_newly_covered_elements)
            max_covered_value = effective_interval_start + num_newly_covered_elements
        return total_distinct_elements

        
        # brute force
        res = set()
        nums.sort()
        for num in nums:
            for i in range(-k, k + 1, 1):
                if num + i not in res:
                    res.add(num + i)
                    break
        return len(res)
