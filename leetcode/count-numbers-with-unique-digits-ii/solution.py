class Solution:
    def numberCount(self, a: int, b: int) -> int:
        count = 0
        for i in range(a, b + 1):
            number = str(i)
            is_unique = len(number) == len(set(number))

            if is_unique:
                count+=1
        return count
