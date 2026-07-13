class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        n = len(s)
        res = ""
        for i in range((n // k) + 1):
            if i % 2 == 0:
                res += s[i*k:min(n,i*k+k)][::-1]
            else:
                res += s[i*k:min(n,i*k+k)]
            print(i * k, i * k + k)
        return res
