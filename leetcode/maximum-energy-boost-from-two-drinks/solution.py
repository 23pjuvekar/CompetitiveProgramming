class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        memo = {} # (i, lastdrink)

        def dp(i, drink):
            if i < 0:
                return 0
            if (i, drink) in memo:
                return memo[(i, drink)]
            if drink == "A":
                memo[(i, "A")] = max(energyDrinkA[i] + dp(i - 1, "A"), dp(i - 1, "B"))
                return memo[(i, "A")]
            else:
                memo[(i, "B")] = max(energyDrinkB[i] + dp(i - 1, "B"), dp(i - 1, "A"))
                return memo[(i, "B")]
        
        return max(dp(n - 1, "A"), dp(n - 1, "B"))
