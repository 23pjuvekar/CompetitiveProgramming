class Solution:
    def maximumXor(self, s: str, t: str) -> str:

        count = Counter(t)
        res = ""
        for c in s:
            if c == "1":
                if count["0"] != 0:
                    res += "1"
                    count["0"] -= 1
                else:
                    res += "0"
                    count["1"] -= 1
            elif c == "0":
                if count["1"] != 0:
                    res += "1"
                    count["1"] -= 1
                else:
                    res += "0"
                    count["0"] -= 1
        return res
