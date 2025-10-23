class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        ans = 0
        pre = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        cnts = [0] * 10
        for i in range(n):
            c = int(s[i])
            if i:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i - 1][j][k] 
                        if k == c: pre[i][j][k] += cnts[j]
            cnts[c] += 1
        suf = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        cnts = [0] * 10
        for i in range(n - 1, -1, -1):
            c = int(s[i])
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suf[i][j][k] = suf[i + 1][j][k]
                        if k == c: suf[i][j][k] += cnts[j]
            cnts[c] += 1
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    ans += pre[i - 1][j][k] * suf[i + 1][j][k]
        return ans % mod
        