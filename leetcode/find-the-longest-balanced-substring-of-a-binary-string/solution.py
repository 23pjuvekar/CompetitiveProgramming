class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        l = 0
        z_d = False
        z_c = 0
        o_c = 0
        res = 0

        for r in range(len(s)):
            if s[r] == "0" and z_d == True:
                l = r
                z_d = False
                z_c = 1
                o_c = 0
            elif s[r] == "1":
                o_c += 1
                z_d = True
            elif s[r] == "0":
                z_c += 1
            print(r, l, z_d)
            if z_d:
                res = max(res, 2 * min(z_c, o_c))
        if z_d:
            res = max(res, 2 * min(z_c, o_c))
        return res
