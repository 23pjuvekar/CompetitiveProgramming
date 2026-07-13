class Solution:
    def minOperations(self, s: str) -> int:
        s = list(s)
        res = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if s[i] == "0":
                    s[i+1] = "1"
                else:
                    s[i+1] = "0"
                res += 1
        return min(res, len(s) - res)
