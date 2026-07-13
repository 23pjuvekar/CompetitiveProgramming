class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        M = len(potions)
        res = []
        for i in range(len(spells)):
            value_need = success / spells[i]
            res.append(M - bisect_left(potions, value_need))
        return res
