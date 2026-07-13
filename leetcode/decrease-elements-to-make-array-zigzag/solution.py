class Solution(object):
    def movesToMakeZigzag(self, nums):
        def get_moves(start_even):
            moves = 0
            for i in range(len(nums)):
                if i % 2 == start_even:
                    left = nums[i - 1] if i > 0 else float('inf')
                    right = nums[i + 1] if i + 1 < len(nums) else float('inf')
                    min_adj = min(left, right)
                    if nums[i] >= min_adj:
                        moves += nums[i] - min_adj + 1

            return moves
        
        return min(get_moves(0), get_moves(1))
