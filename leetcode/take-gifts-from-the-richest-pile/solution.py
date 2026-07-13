class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        g = [-n for n in gifts]
        heapify(g)
        
        while k:
            val = -heappop(g)
            heappush(g, -int(val ** 0.5))
            k -= 1
        return -sum(g)
