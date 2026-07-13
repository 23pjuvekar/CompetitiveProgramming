class Solution:
    def maxDiff(self, num: int) -> int:
        min_value = float("inf")
        max_value = float("-inf")
        for x in "0123456789":
            for y in "0123456789":
                possible = str(num).replace(x, y)
                if possible[0] == "0":
                    continue
                min_value = min(min_value, int(possible))
                max_value = max(max_value, int(possible))
        return max_value - min_value
