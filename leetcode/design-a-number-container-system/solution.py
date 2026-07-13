class NumberContainers:

    def __init__(self):
        self.idx_to_num = {}
        self.num_to_heaps = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number
        heapq.heappush(self.num_to_heaps[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_heaps:
            return -1
            
        heap = self.num_to_heaps[number]
        
        while heap and self.idx_to_num.get(heap[0], float("inf")) != number:
            heapq.heappop(heap)
            
        return heap[0] if heap else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
