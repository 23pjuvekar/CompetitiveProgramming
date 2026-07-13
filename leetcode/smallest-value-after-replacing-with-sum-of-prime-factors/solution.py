class Solution:
    def smallestValue(self, n: int) -> int:

        def getSumPrimes(num):
            s = 0
            d = 2
            temp = num
            while d <= temp:
                while temp % d == 0:
                    s += d
                    temp //= d
                d += 1
            return s
        while True:
            new_n = getSumPrimes(n)
            if new_n == n:
                return n
            n = new_n
