import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added_heap = []
        self.added_set = set()          

    def popSmallest(self) -> int:
        if self.added_heap:
            smallest = heapq.heappop(self.added_heap)
            self.added_set.remove(smallest)
            return smallest
        else:
            result = self.curr
            self.curr += 1
            return result        

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added_set:
            heapq.heappush(self.added_heap, num)
            self.added_set.add(num)
