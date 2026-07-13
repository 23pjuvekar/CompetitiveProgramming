class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        
        facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        n_str = str(n)
        res = 0
        for c in n_str:
            res += facts[int(c)]
        return Counter(str(res)) == Counter(n_str)
