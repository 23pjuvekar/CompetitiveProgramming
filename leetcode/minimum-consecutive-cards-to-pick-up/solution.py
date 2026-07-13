class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        res = float("inf")
        index = {}

        for i in range(len(cards)):
            c = cards[i]
            if c in index:
                res = min(res, i - index[c] + 1)
            index[c] = i
        if res == float("inf"):
            return -1
        return res
