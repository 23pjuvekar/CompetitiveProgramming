class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        key_c = {}
        alp = list("abcdefghijklmnopqrstuvwxyz")
        i = 0
        for c in key:
            if c != " " and c not in key_c:
                key_c[c] = alp[i]
                i += 1
                if i == 26:
                    break
        res = ""
        for m in message:
            if m == " ":
                res += m
            else:
                res += key_c[m]
        return res
