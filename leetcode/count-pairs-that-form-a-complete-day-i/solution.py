class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:

        counter = defaultdict(int)
        res = 0
        for hour in hours:
            counter[hour % 24] += 1

        if counter[0] != 0:
            res += (counter[0] * (counter[0] - 1)) // 2
        if counter[12] != 0:
            res += (counter[12] * (counter[12] - 1)) // 2

        for i in range(1, 12):
            res += (counter[i] * counter[24 - i])
        
        return res
