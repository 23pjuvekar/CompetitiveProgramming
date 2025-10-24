class Solution:
    def minOperations(self, nums: list[int], x: int, y: int) -> int:
        min_operations_left = 1
        max_operations_right = (max(nums) // y) + 1
        x_prime = x - y
        while min_operations_left <= max_operations_right:
            mid_operations = (min_operations_left + max_operations_right) // 2
            remaining_x_decrements_budget = mid_operations
            for current_num_value in nums:
                min_y_decrements_needed = (current_num_value + (y - 1)) // y
                if mid_operations < min_y_decrements_needed:
                    required_additional_x_decrements = (current_num_value - (mid_operations * y) + (x_prime - 1)) // x_prime
                    remaining_x_decrements_budget -= required_additional_x_decrements
                    if remaining_x_decrements_budget < 0:
                        break
            if remaining_x_decrements_budget >= 0:
                max_operations_right = mid_operations - 1
            else:
                min_operations_left = mid_operations + 1
        return max_operations_right + 1