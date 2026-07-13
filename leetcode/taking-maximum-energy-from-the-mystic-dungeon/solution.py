class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        energy.reverse()
        res = float("-inf")
        for i in range(k):
            curr = i
            curr_total = 0
            while curr < len(energy):
                curr_total += energy[curr]
                res = max(res, curr_total)
                curr += k
        return res
