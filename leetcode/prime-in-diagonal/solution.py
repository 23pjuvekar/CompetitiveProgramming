class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        d = []
        n = len(nums)
        for r in range(n):
            for c in range(n):
                if r == c:
                    d.append(nums[r][c])
                elif r + c + 1 == n:
                    d.append(nums[r][c])
        res = 0
        for c in d:
            bad = False
            for i in range(2, int(c ** 0.5) + 1):
                if c % i == 0:
                    bad = True
                    break
            if not bad:
                res = max(res, c)
        if res == 1:
            return 0
        return res
