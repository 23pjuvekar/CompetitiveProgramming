class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        requests = [0] * k
        available = list(range(k))
        heapq.heapify(available)
        busy = []
        for i in range(len(arrival)):
            start = arrival[i]
            length = load[i]
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                heapq.heappush(available, i + ((server - i) % k))
            if not available:
                continue
            server = heapq.heappop(available) % k
            requests[server] += 1
            heapq.heappush(busy, (start + length, server))
        max_requests = max(requests)
        return [i for i, req in enumerate(requests) if req == max_requests]
