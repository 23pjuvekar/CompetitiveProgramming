class Solution:
    def resultingString(self, s: str) -> str:

        def are_consecutive(char1, char2):
            ord1 = ord(char1)
            ord2 = ord(char2)
            if abs(ord1 - ord2) == 1:
                return True
            if (char1 == 'a' and char2 == 'z') or (char1 == 'z' and char2 == 'a'):
                return True
            return False

        while True:
            stack = []
            changed = False
            for char in s:
                if stack and are_consecutive(stack[-1], char):
                    stack.pop()
                    changed = True
                else:
                    stack.append(char)
            new_s = "".join(stack)
            if not changed:
                break
            s = new_s
        return s
