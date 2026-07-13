class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        total = 0

        while mainTank:
            total += 1
            mainTank -= 1
            if total % 5 == 0 and total and additionalTank:
                mainTank += 1
                additionalTank -= 1
        return total * 10
