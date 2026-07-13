class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        value_map = {}
        for key, val in knowledge:
            value_map[key] = val
        i = 0
        res = ""
        while i < len(s):
            if s[i] == "(":
                i += 1
                replace = ""
                while s[i] != ")":
                    replace += s[i]
                    i += 1
                if replace not in value_map:
                    res += "?"
                else:
                    res += value_map[replace]
                i += 1
            else:
                res += s[i]
                i += 1
        return res
