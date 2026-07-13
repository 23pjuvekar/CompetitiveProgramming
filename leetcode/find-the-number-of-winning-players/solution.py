class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        c1 = [defaultdict(int) for _ in range(n)]

        for i, b in pick:
            c1[i][b] += 1
        
        res = 0
        for i in range(n):
            for key, val in c1[i].items():
                if val > i:
                    res += 1
                    break
        return res
