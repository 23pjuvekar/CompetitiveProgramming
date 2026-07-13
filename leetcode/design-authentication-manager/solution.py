class AuthenticationManager:

    def __init__(self, timeToLive: int): 
        self.q = deque() # [time, tokenID]
        self.count = defaultdict(int)
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expireTokens(currentTime)
        self.q.append([currentTime + self.timeToLive, tokenId])
        self.count[tokenId] += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.expireTokens(currentTime)
        if tokenId in self.count:
            self.q.append([currentTime + self.timeToLive, tokenId])
            self.count[tokenId] += 1

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.expireTokens(currentTime)
        return len(self.count)

    def expireTokens(self, currentTime: int) -> int:
        while self.q and self.q[0][0] <= currentTime:
            _, tokenId = self.q.popleft()
            self.count[tokenId] -= 1
            if self.count[tokenId] == 0:
                del self.count[tokenId]

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
