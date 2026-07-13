class Solution:
    def isFascinating(self, n: int) -> bool:

        string = str(n) + str(n * 2) + str(n * 3)

        return len(set(string)) == 9 and "0" not in string and len(string) == 9
