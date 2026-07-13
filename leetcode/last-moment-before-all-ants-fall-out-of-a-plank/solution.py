class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        right_min = float("inf")
        for num in right:
            right_min = min(right_min, num)
        left_max = 0
        for num in left:
            left_max = max(left_max, num)
        
        return max(n - right_min, left_max)
