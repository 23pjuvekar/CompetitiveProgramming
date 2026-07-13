class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        res = -1
        number_string = str(number)

        print(number_string[2:])

        for i in range(len(number_string)):
            if number_string[i] == digit:
                res = max(res, int(number_string[:i] + number_string[i+1:]))
            

        return str(res)
