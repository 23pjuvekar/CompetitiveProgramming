class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        s = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            s[fruits[r]] += 1
            while len(s) > 2:
                s[fruits[l]] -= 1
                if s[fruits[l]] == 0:
                    del s[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
