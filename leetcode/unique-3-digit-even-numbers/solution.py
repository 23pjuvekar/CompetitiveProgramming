class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        numbers = set()
        n = len(digits)
        for i in range(n):
            a = digits[i]
            for j in range(n):
                b = digits[j]
                for l in range(n):
                    c = digits[l]
                    if i != j and i != l and j != l and a != 0 and c % 2 == 0:
                        numbers.add((a, b, c))
        return len(numbers)
