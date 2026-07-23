class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def trips_completed(t: int) -> int:
            return sum(t // bus_time for bus_time in time)

        lo, hi = 1, min(time) * totalTrips

        while lo < hi:
            mid = (lo + hi) // 2
            if trips_completed(mid) >= totalTrips:
                hi = mid
            else:
                lo = mid + 1

        return hi
