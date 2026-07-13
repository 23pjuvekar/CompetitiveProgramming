class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        prev = -1
        res = 0
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    res = max(i, res)
                else:
                    res = max(abs(i - prev) // 2, res)
                prev = i
        return max(res, (n - 1) - prev)
