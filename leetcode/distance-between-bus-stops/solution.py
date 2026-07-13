class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        total = sum(distance)
        o1 = 0
        if start < destination:
            o1 = sum(distance[start:destination])
        else:
            o1 = sum(distance[destination:start])
        return min(total - o1, o1)
