class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """


        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_one = heapq.heappop(stones)
            stone_two = heapq.heappop(stones)
            if stone_one < stone_two:
                heapq.heappush(stones, stone_one - stone_two)

        stones.append(0)
        return -1 * stones[0]
