class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()

        c_free = 1
        res = 0

        for start, end in meetings:
            if c_free < start:
                res += (start - c_free)
            c_free = max(end + 1, c_free)
        if c_free <= days:
            res += (1 + days - c_free)
        return res
