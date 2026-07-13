class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        heapify(tasks)
        res = []

        while tasks:
            v1 = heappop(tasks)
            v2 = heappop(tasks)
            v3 = heappop(tasks)
            v4 = heappop(tasks)
            res.append(max(v1, v2, v3, v4))
        
        processorTime.sort(reverse=True)
        final = 0
        for x, y in zip(processorTime, res):
            final = max(final, x + y)
        return final
