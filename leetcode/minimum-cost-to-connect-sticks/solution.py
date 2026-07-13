class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)
            heapq.heappush(sticks, stick_1 + stick_2)
            res += stick_1 + stick_2
        return res
