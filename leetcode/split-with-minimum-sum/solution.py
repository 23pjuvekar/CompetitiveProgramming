class Solution:
    def splitNum(self, num: int) -> int:

        values = []
        while num:
            values.append(num % 10)
            num = num // 10
        values.sort(reverse=True)

        res = 0
        mult = 1
        for i in range(len(values)):
            if i % 2 == 0 and i != 0:
                mult *= 10
            res += values[i] * mult
        return res
