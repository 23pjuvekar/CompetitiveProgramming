class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        if num == 0:
            return "0"
        num_sign = num // abs(num)
        num = abs(num)
        while num > 0:
            res += str(num % 7)
            num = num // 7
        res = res[::-1]
        if num_sign == -1:
            return "-" + res
        return res
