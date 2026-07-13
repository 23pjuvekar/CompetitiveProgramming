class Solution:
    def secondHighest(self, s: str) -> int:
        res = set()
        for c in s:
            if c.isdigit():
                res.add(c)
        if len(res) < 2:
            return -1
        res = list(res)
        res.sort(reverse=True)
        return int(res[1])
