class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:

        seen = set()
        res = 0

        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                res += 1
                seen.clear()
        return res + 1
