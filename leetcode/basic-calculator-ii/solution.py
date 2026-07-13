class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        pre_op = '+'
        s += "+"
        stack = []

        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    temp = stack.pop()
                    stack.append(temp*num)
                elif pre_op == '/':
                    temp = stack.pop()
                    stack.append(math.trunc(temp/num))
                num = 0
                pre_op = c
        return sum(stack)
