class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        minHeap = []
        for x, y in points:
            dist = (x * x) + (y * y)
            minHeap.append(((dist, x, y)))

        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res
