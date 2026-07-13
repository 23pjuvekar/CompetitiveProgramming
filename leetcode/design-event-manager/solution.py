class EventManager:

    def __init__(self, events: list[list[int]]):
        self.heap = []
        self.event_map = {}
        for eventId, priority in events:
            self.event_map[eventId] = priority
            heappush(self.heap, (-priority, eventId))
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.event_map[eventId] = newPriority
        heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            neg_p, eventId = heappop(self.heap)
            if eventId in self.event_map and self.event_map[eventId] == -neg_p:
                del self.event_map[eventId]
                return eventId
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
