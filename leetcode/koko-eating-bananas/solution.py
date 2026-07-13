class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hoursToEat(amount):
            res = 0
            for pile in piles:
                res += math.ceil(float(pile) / amount)
            return res


        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            time = hoursToEat(m)
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
