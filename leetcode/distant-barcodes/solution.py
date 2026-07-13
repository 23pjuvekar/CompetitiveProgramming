class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        """
        max_heap = []
        heapify(max_heap)
        for key, val in Counter(barcodes).items():
            heapq.heappush(max_heap, [-val, key])
        res = []
        wait = []
        while max_heap:
            # print(max_heap, res, wait)
            amt, val = heapq.heappop(max_heap)
            amt *= -1
            res.append(val)
            if wait != []:
                heapq.heappush(max_heap, wait)
            if amt - 1 > 0:
                wait = [-(amt - 1), val]
            else:
                wait = []
        return res
        """

        count = Counter(barcodes)
        sorted_barcodes = sorted(count.items(), key=lambda x: -x[1])

        n = len(barcodes)
        res = [0] * n
        index = 0
        for code, freq in sorted_barcodes:
            for _ in range(freq):
                if index >= n:
                    index = 1
                res[index] = code
                index += 2
        return res
