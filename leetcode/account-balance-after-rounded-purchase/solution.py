class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:

        amt = purchaseAmount - (purchaseAmount % 10)
        if purchaseAmount % 10 != 0 and purchaseAmount % 10 > 4:
            amt += 10
        return 100 - amt
