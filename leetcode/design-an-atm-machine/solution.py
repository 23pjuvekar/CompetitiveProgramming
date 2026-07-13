class ATM:
    denominations = [20, 50, 100, 200, 500]

    def __init__(self):
        self.counts = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        self.counts = [held + added for held, added in zip(self.counts, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        dispensed = [0] * 5
        for i in range(4, -1, -1):
            dispensed[i] = min(self.counts[i], amount // self.denominations[i])
            amount -= dispensed[i] * self.denominations[i]
        if amount != 0:
            return [-1]
        self.counts = [held - taken for held, taken in zip(self.counts, dispensed)]
        return dispensed
