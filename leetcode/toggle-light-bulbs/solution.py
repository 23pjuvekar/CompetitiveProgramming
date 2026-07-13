class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:

        counts = defaultdict(int)
        for bulb in bulbs:
            counts[bulb] += 1
        res = []
        for bulb, switch_amt in counts.items():
            if switch_amt % 2 == 1:
                res.append(bulb)
        res.sort()
        return res
