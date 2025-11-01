class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        finalStack = numStack[:-k] if k else numStack
        result = "".join(finalStack)
        stripped_result = ""
        leading_zero_stripped = False
        for char_digit in result:
            if char_digit == '0' and not leading_zero_stripped:
                continue
            else:
                stripped_result += char_digit
                leading_zero_stripped = True

        return stripped_result if stripped_result else "0"