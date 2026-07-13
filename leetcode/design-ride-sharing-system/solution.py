class RideSharingSystem:

    def __init__(self):
        self.drivers = deque()
        self.riders = deque()
        self.waiting = set()
        self.cancelled = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] in self.cancelled:
            rid = self.riders.popleft()
            self.cancelled.remove(rid)
            self.waiting.remove(rid)

        if self.riders and self.drivers:
            did = self.drivers.popleft()
            rid = self.riders.popleft()
            self.waiting.remove(rid)
            return [did, rid]

        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.waiting:
            self.cancelled.add(riderId)
