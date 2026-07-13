class Solution:
    def largestPrime(self, n: int) -> int:

        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        
        primes = [p for p, prime in enumerate(is_prime) if prime]

        current_sum = 0
        ans = 0
        for p in primes:
            current_sum += p
            if current_sum > n:
                break
            if is_prime[current_sum]:
                ans = current_sum
                
        return ans
