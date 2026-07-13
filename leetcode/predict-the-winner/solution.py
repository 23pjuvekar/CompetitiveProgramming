class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def get_max_diff(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == j:
                return nums[i]
            
            take_left = nums[i] - get_max_diff(i + 1, j)
            take_right = nums[j] - get_max_diff(i, j - 1)

            memo[(i, j)] = max(take_left, take_right)
            return memo[(i, j)]

        return get_max_diff(0, n - 1) >= 0
