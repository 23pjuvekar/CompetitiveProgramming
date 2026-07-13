class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return math.ceil(n / 2) * math.floor(m / 2) + math.floor(n / 2) * math.ceil(m / 2)
