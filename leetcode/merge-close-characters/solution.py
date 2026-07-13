class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:

        stack = []
        for c in s:
            if stack and c in stack[-min(len(stack), k):]:
                continue
            else:
                stack.append(c)
        return "".join(stack)
