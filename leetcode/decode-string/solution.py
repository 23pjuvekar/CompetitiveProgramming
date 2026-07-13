class Solution:
    def decodeString(self, s: str) -> str:

        digits = set("1234567890")

        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                word = ""
                while stack and stack[-1] != "[":
                    word += stack[-1][::-1] # pop until word in collected
                    stack.pop()
                stack.pop() # remove "["
                word = word[::-1] #reverse word
                cnt = ""
                while stack and stack[-1] in digits:
                    cnt += stack[-1]
                    stack.pop()
                cnt = cnt[::-1]
                word_final = ""
                for i in range(int(cnt)):
                    word_final += word
                stack.append(word_final)
            print(stack)
        print(stack)
        return "".join(stack)
