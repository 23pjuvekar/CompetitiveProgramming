from collections import deque


class FrontMiddleBackQueue:
    def __init__(self):
        self.front_half = deque()
        self.back_half = deque()

    def _shift_to_back(self):
        if len(self.front_half) > len(self.back_half):
            self.back_half.appendleft(self.front_half.pop())

    def _shift_to_front(self):
        if len(self.back_half) > len(self.front_half) + 1:
            self.front_half.append(self.back_half.popleft())

    def pushFront(self, val):
        self.front_half.appendleft(val)
        self._shift_to_back()

    def pushMiddle(self, val):
        self.front_half.append(val)
        self._shift_to_back()

    def pushBack(self, val):
        self.back_half.append(val)
        self._shift_to_front()

    def popFront(self):
        if not self.front_half and not self.back_half:
            return -1
        if not self.front_half:
            return self.back_half.popleft()
        value = self.front_half.popleft()
        self._shift_to_front()
        return value

    def popMiddle(self):
        if not self.front_half and not self.back_half:
            return -1
        if len(self.front_half) == len(self.back_half):
            return self.front_half.pop()
        return self.back_half.popleft()

    def popBack(self):
        if not self.front_half and not self.back_half:
            return -1
        value = self.back_half.pop()
        self._shift_to_back()
        return value
