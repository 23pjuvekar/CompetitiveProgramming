class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        heap = []
        for p, t in classes:
            gain = (p + 1) / (t + 1) - (p / t)
            heapq.heappush(heap, (-gain, p, t))
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            new_gain = (p + 1) / (t + 1) - (p / t)
            heapq.heappush(heap, (-new_gain, p, t))
            
        total_ratio = 0
        for _, p, t in heap:
            total_ratio += (p / t)
            
        return total_ratio / len(classes)
