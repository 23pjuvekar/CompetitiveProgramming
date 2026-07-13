class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        c1 = Counter(arr)
        h = []

        for key, amt in c1.items():
            heappush(h, -amt)
        
        res = 0
        gone = 0
        while gone < len(arr) // 2:
            gone += -heappop(h)
            res += 1
        return res
