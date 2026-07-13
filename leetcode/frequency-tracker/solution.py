class FrequencyTracker:

    def __init__(self):
        self.mp = defaultdict(int)
        self.freq = defaultdict(set)

    def add(self, number: int) -> None:
        if self.mp[number] != 0:
            self.freq[self.mp[number]].remove(number)
        self.mp[number] += 1
        self.freq[self.mp[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if self.mp[number] != 0:
            self.freq[self.mp[number]].remove(number)
            self.mp[number] -= 1
            self.freq[self.mp[number]].add(number)


    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq[frequency]) != 0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
