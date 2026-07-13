class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        
        if n == 1:
            return 1

        n_sub_1 = 0
        n_sub_2 = 1

        for i in range(2, n+1):
            temp = n_sub_2
            n_sub_2 = n_sub_2 + n_sub_1
            n_sub_1 = temp
        
        return n_sub_2
