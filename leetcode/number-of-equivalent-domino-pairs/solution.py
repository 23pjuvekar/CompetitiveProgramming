class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        values = defaultdict(int)
        res = 0
        for a, b in dominoes:
            res += values[(a, b)]
            if a != b:
                res += values[(b, a)]
            values[(a, b)] += 1
        return res
