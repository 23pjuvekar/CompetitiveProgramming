class Solution:
    def minOperations(self, nums: list[int]) -> int:

        MAX_VAL = 10 ** 5 + 500 
        is_prime = [True] * (MAX_VAL + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(MAX_VAL**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, MAX_VAL + 1, p):
                    is_prime[i] = False
                    
        total_ops = 0
        for i, x in enumerate(nums):
            curr = x
            if i % 2 == 0:
                while not is_prime[curr]:
                    curr += 1
            else:
                while is_prime[curr]:
                    curr += 1
            total_ops += (curr - x)
                
        return total_ops
