class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        min_x = m
        min_y = n
        for x, y in ops:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
        return min_x * min_y

        