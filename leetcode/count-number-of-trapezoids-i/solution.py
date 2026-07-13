class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        def pickTwoFormula(amt):
            return ((amt) * (amt - 1) // 2) % MOD

        """
        0: 1, 2, 3 --> 2(1), 1(2) --> 3
        2: 2, 3 --> 1(1) --> 3
        """

        MOD = 10**9 + 7

        level_map = defaultdict(int)
        for x, y in points:
            level_map[y] += 1
        
        level_amt = []
        total_sum = 0
        for key, amt in level_map.items():
            level_amt.append( pickTwoFormula(amt) )
            total_sum += pickTwoFormula(amt)
        
        res = pickTwoFormula(total_sum)
        for i in range(len(level_amt)):
            res -= pickTwoFormula(level_amt[i])
        return res % MOD
