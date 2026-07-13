class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        length = max(len(num1), len(num2))
        res = ""
        num1 = num1[::-1]
        num2 = num2[::-1]

        carry = 0
        for i in range(length):
            n1 = 0
            n2 = 0
            if i < len(num1):
                n1 = int(num1[i])
            if i < len(num2):
                n2 = int(num2[i])
            num = n1 + n2 + carry
            carry = num // 10
            num = num % 10
            res += str(num)
        
        if carry != 0:
            res += str(carry)
        
        return res[::-1]
