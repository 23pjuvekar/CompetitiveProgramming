class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        def fact(number):
            res = 1
            for i in range(1, number + 1):
                res *= i
            return res

        c1 = Counter(complexity)
        if min(complexity) != complexity[0] or c1[complexity[0]]!= 1:
            return 0
        n = len(complexity) - 1
        res = fact(n) 
        # for k, v in c1.items():
        #     res = res // (fact(v))
        return res % (10**9 + 7)
