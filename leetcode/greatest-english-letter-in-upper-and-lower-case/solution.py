class Solution:
    def greatestLetter(self, s: str) -> str:

        value = defaultdict(set)
        res = ""

        for c in s:
            value[c.lower()].add(c)
            if len(value[c.lower()]) == 2:
                if res == "":
                    res = c.upper()
                else:
                    if ord(res) < ord(c.upper()):
                        res = c.upper()
        return res
