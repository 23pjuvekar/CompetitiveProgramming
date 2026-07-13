class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:

        return math.ceil(n / (1 + 2 * k)) * math.ceil(m / (1 + 2 * k))
