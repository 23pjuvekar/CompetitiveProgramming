class Router:

    def __init__(self, memoryLimit: int):
        self.s = set()
        self.q = deque()
        self.l = memoryLimit
        self.mp = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.s:
            return False
        self.s.add((source, destination, timestamp))
        self.q.append([source, destination, timestamp])
        self.mp[destination].append(timestamp)
        if len(self.s) > self.l:
            val = self.q.popleft()
            self.s.remove((val[0], val[1], val[2]))
            self.mp[val[1]].pop(0)
        return True
        
    def forwardPacket(self) -> List[int]:
        if self.q:
            val = self.q.popleft()
            self.s.remove((val[0], val[1], val[2]))
            self.mp[val[1]].pop(0)
            return val
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.mp:
            return 0
        packets_for_dest = self.mp[destination]
        start_idx = bisect.bisect_left(packets_for_dest, startTime)
        end_idx = bisect.bisect_right(packets_for_dest, endTime)
        
        return end_idx - start_idx

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
