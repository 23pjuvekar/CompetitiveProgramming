class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        months_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_convert(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(months_day[:month - 1]) + day
        days = min(date_convert(leaveBob), date_convert(leaveAlice)) - max(date_convert(arriveBob), date_convert(arriveAlice)) + 1
        if days > 0:
            return days
        return 0
