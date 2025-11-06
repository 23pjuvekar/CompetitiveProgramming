class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj_matrix = defaultdict(list)
        for station1, station2 in connections:
            adj_matrix[station1].append(station2)
            adj_matrix[station2].append(station1)

        online = set(list(range(1, c + 1)))
        station_to_group = defaultdict(int)
        min_heaps = defaultdict(list)

        def dfs(station, head):
            if station_to_group[station]:
                return
            station_to_group[station] = head
            heapq.heappush(min_heaps[head], station)
            for nei_stations in adj_matrix[station]:
                dfs(nei_stations, head)

        for station in range(1, c + 1):
            dfs(station, station)

        res = []
        for check_type, station in queries:
            if check_type == 1:
                if station in online:
                    res.append(station)
                else:
                    group = station_to_group[station]
                    min_heap = min_heaps[group]
                    while min_heap and min_heap[0] not in online:
                        heapq.heappop(min_heap)
                    if not min_heap:
                        res.append(-1)
                    else:
                        res.append(min_heap[0])
            elif station in online:
                online.remove(station)

        return res