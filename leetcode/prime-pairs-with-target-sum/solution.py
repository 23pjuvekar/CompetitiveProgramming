class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 4:
            return []

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        
        res = []
        for x in range(1, n // 2 + 1):
            y = n - x
            if is_prime[x] and is_prime[y]:
                res.append([x, y])
        return res



        """
        def isPrime(number):
            if number == 1:
                return False
            for divisor in range(2, int(number ** 0.5) + 1):
                if number % divisor == 0:
                    return False
            return True

        res = []
        for x in range(1, n // 2 + 1):
            y = n - x
            if isPrime(x) and isPrime(y):
                res.append([x, y])
        return res
        """
