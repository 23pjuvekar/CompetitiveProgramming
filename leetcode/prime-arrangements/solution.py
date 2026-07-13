class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def factorial(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        pcount = 0
        for num in range(1, n + 1):
            if is_prime(num):
                pcount += 1

        return factorial(pcount) * factorial(n - pcount) % (10**9 + 7)
