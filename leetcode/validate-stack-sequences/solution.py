class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        pushed = deque(pushed)
        popped = deque(popped)
        while pushed or popped:
            if stack and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
            elif pushed:
                stack.append(pushed.popleft())
            else:
                break
        return len(stack) == 0 and len(pushed) == 0 and len(popped) == 0
