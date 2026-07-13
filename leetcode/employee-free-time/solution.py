"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        all_intervals = []
        for employee_schedule in schedule:
            for interval in employee_schedule:
                all_intervals.append(interval)

        merged = []
        all_intervals.sort(key=lambda x: x.start)
        prev_s, prev_e = all_intervals[0].start, all_intervals[0].end
        for sch in all_intervals:
            start = sch.start
            end = sch.end
            if prev_e >= start:
                prev_e = max(prev_e, end)
            else:
                merged.append([prev_s, prev_e])
                prev_s = start
                prev_e = end
        merged.append([prev_s, prev_e])
        prev_start = merged[0][1]
        res = []
        for start, end in merged[1:]:
            res.append(Interval(prev_start, start))
            prev_start = end
        return res
