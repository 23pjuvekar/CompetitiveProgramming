class HitCounter:

    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        start = timestamp
        end = timestamp + 299
        self.hits.append([start, end])
        
    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][1] < timestamp:
            self.hits.popleft()
        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
