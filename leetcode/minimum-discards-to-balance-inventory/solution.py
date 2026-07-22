class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        window = deque()
        count = {}
        discards = 0

        for i, t in enumerate(arrivals):
            while window and window[0] < i - w + 1:
                old_day = window.popleft()
                old_type = arrivals[old_day]
                count[old_type] -= 1
                if count[old_type] == 0:
                    del count[old_type]

            if count.get(t, 0) < m:
                count[t] = count.get(t, 0) + 1
                window.append(i)
            else:
                discards += 1

        return discards
