class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        amount = 0

        for c in s:
            if c == letter:
                amount += 1

        return (amount * 100) // len(s)
