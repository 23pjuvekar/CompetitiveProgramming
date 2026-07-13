class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        def isPrime(number):
            if number <= 1:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True
        
        primes = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if isPrime(int(substring)):
                    primes.add(int(substring))
        primes = list(primes)
        primes.sort(reverse=True)
        amt = min(3, len(primes))
        return sum(primes[:amt])
