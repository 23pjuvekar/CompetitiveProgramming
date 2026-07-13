class Solution:
    def checkDivisibility(self, n: int) -> bool:

        curr_sum = 0
        curr_product = 1
        for c in str(n):
            curr_sum += int(c)
            curr_product *= int(c)
        return n % (curr_sum + curr_product) == 0
