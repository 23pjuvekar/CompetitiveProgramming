class Solution:
    def smallestString(self, s: str) -> str:

        a_c = 0
        n_a = False
        res = list(s)

        for i in range(len(s)):
            if s[i] == "a" and n_a:
                a_c += 1
                if a_c == 1:
                    return "".join(res)
            elif s[i] != "a":
                n_a = True
                res[i] = chr(ord(res[i]) - 1)
        
        if a_c == 0 and n_a == False:
            res[-1] = "z"
        return "".join(res)
