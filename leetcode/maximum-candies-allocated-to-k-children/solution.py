class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        l = 0
        r = sum(candies) // k
        res = 0

        def good(amt):
            if amt == 0:
                return True
            curr = k
            for c in candies:
                curr -= (c // amt)
            return curr <= 0

        while l <= r:
            m = (l + r) // 2
            if good(m):
                l = m + 1
                res = m
            else:
                r = m - 1
        return res
