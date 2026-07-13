class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heap = []

        for stone in piles:
            heap.append(-stone)

        heapq.heapify(heap)

        while k > 0:
            max_item = -heap[0]
            heapq.heappop(heap)
            new_item = max_item - (max_item // 2)
            if new_item % 2 == 0:
                heapq.heappush(heap, -new_item)
            else:
                heapq.heappush(heap, -new_item)
            k -= 1

        return -sum(heap)
