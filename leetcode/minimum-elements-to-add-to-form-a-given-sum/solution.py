class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:

        total = abs(sum(nums) - goal) / limit
        return ceil(total)
