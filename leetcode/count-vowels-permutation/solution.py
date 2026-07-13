class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        a = e[i] + u[i] + i[i]
        e = a[i] + i[i]
        i = o[i] + e[i]
        o = i[i]
        u = o[i] + i[i]
        """

        dp = defaultdict(int)
        dp["a"] = 1
        dp["e"] = 1
        dp["i"] = 1
        dp["o"] = 1
        dp["u"] = 1
        m = (10**9) + 7

        for _ in range(n - 1):
            a = dp["a"]
            e = dp["e"]
            i = dp["i"]
            o = dp["o"]
            u = dp["u"]
            dp["a"] = (e + u + i) % m
            dp["e"] = (a + i) % m
            dp["i"] = (o + e) % m
            dp["o"] = i % m
            dp["u"] = (o + i) % m
        return (dp["a"] + dp["i"] + dp["e"] + dp["o"] + dp["u"]) % m
