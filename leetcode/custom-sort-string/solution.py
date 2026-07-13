class Solution:
    def customSortString(self, order: str, s: str) -> str:

        res = ""
        counter = Counter(s)
        for c in order:
            if c in counter:
                res += c * counter[c]
                del counter[c]
        for c, a in counter.items():
            res += c * a
        return res
