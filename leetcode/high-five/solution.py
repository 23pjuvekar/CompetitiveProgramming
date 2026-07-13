class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        scores = defaultdict(list)

        for item in items:
            heapq.heappush(scores[item[0]], item[1])
            if len(scores[item[0]]) > 5:
                heapq.heappop(scores[item[0]])
        
        res = []

        for idx, heap in scores.items():
            res.append([idx, sum(heap) // len(heap)])
        
        res.sort()

        return res
