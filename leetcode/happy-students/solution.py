class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        total_students = len(nums)
        valid_selections = 0
        for selected_count in range(total_students + 1):
            selected_ok = selected_count == 0 or selected_count > nums[selected_count - 1]
            unselected_ok = selected_count == total_students or selected_count < nums[selected_count]
            if selected_ok and unselected_ok:
                valid_selections += 1
        return valid_selections
