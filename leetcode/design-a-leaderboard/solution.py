class Leaderboard:

    def __init__(self):
        self.mp = {}
        self.data = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.mp: 
            self.data.remove(self.mp[playerId])
            self.mp[playerId] += score 
        else: self.mp[playerId] = score
        self.data.add(self.mp[playerId])

    def top(self, K: int) -> int:
        return sum(self.data[-K:])

    def reset(self, playerId: int) -> None:
        self.data.remove(self.mp[playerId])
        self.mp.pop(playerId)
