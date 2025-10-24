class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        strength = {k: k * count[k] for k in count}
        spells = sorted(list(strength.keys()))
        n = len(spells)
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            # Option 1: Don't take the current spell
            res = dp(i + 1)
            # Option 2: Take the current spell
            current_spell_damage = strength[spells[i]]
            # Find the next valid spell to consider
            j = i + 1
            while j < n and spells[j] <= spells[i] + 2:
                j += 1
            res = max(res, current_spell_damage + dp(j))
            memo[i] = res
            return res

        return dp(0)