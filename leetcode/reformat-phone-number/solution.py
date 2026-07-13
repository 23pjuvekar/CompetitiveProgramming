class Solution:
    def reformatNumber(self, number: str) -> str:

        number = number.replace(" ", "")
        number = number.replace("-", "")
        n = len(number)
        end = ""
        if n % 3 == 1:
            end = number[n-4:n-2] + "-" + number[n-2:n]
            n -= 4
        elif n % 3 == 2:
            end = number[n-2:n+1]
            n -= 2
        res = ""
        for i in range(0, n, 3):
            res += number[i:i+3] + "-"
        if end != "":
            return res + end
        return res[:len(res)-1]
