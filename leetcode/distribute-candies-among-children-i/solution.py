class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for g in range(limit + 1):
                    if i + j + g == n:
                        res += 1
        return res
