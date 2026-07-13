class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []

        for c in s:
            if c == ")":
                reverse = ""
                while stack[-1] != "(":
                    reverse += stack.pop()
                stack.pop()
                stack.extend(reverse)
            else:
                stack.append(c)

        res = ""
        for item in stack:
            res += item

        return res
