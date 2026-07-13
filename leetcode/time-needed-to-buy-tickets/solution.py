class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        amt = tickets[k]
        res = 0
        for i in range(len(tickets)):
            t = tickets[i]
            if i <= k:
                res += min(t, amt)
            else:
                res += min(t, amt - 1)
        return res
