class Solution:
    def myAtoi(self, input: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(input)
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        while index < n and input[index] == " ":
            index += 1
        if index < n and input[index] == "+":
            sign = 1
            index += 1
        elif index < n and input[index] == "-":
            sign = -1
            index += 1
        while index < n and input[index].isdigit():
            digit = int(input[index])
            new_result_potential = result * 10 + digit
            if sign == 1:
                if new_result_potential > INT_MAX:
                    return INT_MAX
            else:
                if new_result_potential * sign < INT_MIN:
                    return INT_MIN
            result = new_result_potential
            index += 1
        return sign * result
