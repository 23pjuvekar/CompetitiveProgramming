class Solution:
    def heightChecker(self, heights: List[int]) -> int:


        expected = heights.copy()
        expected.sort()
        res = 0
        for num1, num2 in zip(heights, expected):
            if num1 != num2:
                res += 1
        return res
