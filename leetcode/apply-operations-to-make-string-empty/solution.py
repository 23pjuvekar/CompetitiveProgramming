class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        count = Counter(s)
        max_value = 0
        for key, val in count.items():
            max_value = max(max_value, val)

        used = set()
        for c in reversed(s):
            if c in used:
                continue
            if count[c] == max_value:
                used.add(c)
        res = ""
        for c in s:
            if c not in used:
                continue
            if count[c] == 1:
                res += c
            count[c] -= 1
        return res
