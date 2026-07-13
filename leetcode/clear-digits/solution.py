class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []
        digits = set("1234567890")

        for c in s:
            if c not in digits:
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
