class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        n = len(arr) - k
        heap = []
        for key, val in Counter(arr).items():
            heappush(heap, -val)
        res = 0
        while n > 0:
            val = heappop(heap)
            n += val
            res += 1
        return res
