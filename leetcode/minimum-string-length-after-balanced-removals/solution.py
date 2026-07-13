class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:

        c = Counter(s)

        return abs(c["a"] - c["b"])
