class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        r = int(str(n)[::-1])
        
        start = min(n, r)
        end = max(n, r)
        
        total_sum = 0
        for i in range(start, end + 1):
            if is_prime(i):
                total_sum += i
        return total_sum
