class Solution:
    def completePrime(self, num: int) -> bool:

        def isPrime(num):
            if num < 2:
                return False
            for x in range(2, int(num ** 0.5) + 1):
                if num % x == 0:
                    return False
            return True

        num_str = str(num)
        n = len(num_str)

        for i in range(1, n + 1):
            if not isPrime(int(num_str[0:i])):
                return False
        
        for i in range(n):
            if not isPrime(int(num_str[i:n])):
                return False
        
        return True
