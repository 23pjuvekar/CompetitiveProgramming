class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        hour = hour % 12

        s_p = hour * 30 + minutes * 0.5
        s_d = 6 * minutes

        diff = abs(s_p - s_d)
        return min(diff, 360 - diff)
