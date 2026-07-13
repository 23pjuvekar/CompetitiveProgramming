class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        attended_events = 0
        day = 1
        min_heap = []
        event_idx = 0
        n = len(events)
        max_end_day = 0
        if events:
            max_end_day = max(end for start, end in events)
        while day <= max_end_day or min_heap:
            while event_idx < n and events[event_idx][0] <= day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                attended_events += 1
            day += 1
        return attended_events
