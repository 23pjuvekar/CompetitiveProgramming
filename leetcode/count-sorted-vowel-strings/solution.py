class Solution:
    def countVowelStrings(self, n: int) -> int:

        dp = defaultdict(int)
        dp["a"] = 1
        dp["e"] = 1
        dp["i"] = 1
        dp["o"] = 1
        dp["u"] = 1
        for i in range(n - 1):
            dp["u"] = dp["u"] + dp["o"] + dp["i"] + dp["e"] + dp["a"]
            dp["o"] = dp["o"] + dp["i"] + dp["e"] + dp["a"]
            dp["i"] = dp["i"] + dp["e"] + dp["a"]
            dp["e"] = dp["e"] + dp["a"]
            dp["a"] = dp["a"]
        return dp["u"] + dp["o"] + dp["i"] + dp["e"] + dp["a"]
