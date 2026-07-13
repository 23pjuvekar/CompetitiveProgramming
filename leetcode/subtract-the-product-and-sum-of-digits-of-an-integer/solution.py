class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum_digit = 0
        product_digit = 1

        for c in str(n):
            sum_digit += int(c)
            product_digit *= int(c)
        
        return product_digit - sum_digit
