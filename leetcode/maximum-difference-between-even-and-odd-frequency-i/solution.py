class Solution:
    def maxDifference(self, string: str) -> int:
        max_odd = -maxsize
        min_even = maxsize

        for freq in Counter(string).values():
            if freq & 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even
