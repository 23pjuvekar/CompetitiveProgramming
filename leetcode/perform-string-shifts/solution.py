class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        q = deque(s)

        for direction, amount in shift:
            if direction == 0:
                for i in range(amount):
                    q.append(q.popleft())
            else:
                for i in range(amount):
                    q.appendleft(q.pop())
        
        return "".join(q)
