class Solution:
    def countPoints(self, rings: str) -> int:

        rods = defaultdict(set)

        for i in range(0, len(rings), 2):
            rods[rings[i + 1]].add(rings[i])
        res = 0
        for key, val in rods.items():
            if len(val) == 3:
                res += 1
        return res
