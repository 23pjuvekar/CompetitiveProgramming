class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        lowest = 0
        highest = 0
        current = 0
        for difference in differences:
            current += difference
            lowest = min(lowest, current)
            highest = max(highest, current)
            if highest - lowest > upper - lower:
                return 0
        return (upper - lower) - (highest - lowest) + 1
