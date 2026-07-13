class Solution:
    def countEven(self, num: int) -> int:

        if sum(map(int, str(num))) % 2 != 0:
            return (num - 1) // 2
        else:
            return num // 2
