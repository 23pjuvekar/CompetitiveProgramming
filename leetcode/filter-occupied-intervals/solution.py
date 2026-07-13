class Solution:
    def filterOccupiedIntervals(self, intervals, filter_start, filter_end):
        intervals.sort()
        merged = []
        current_start, current_end = intervals[0]
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if current_end >= next_start - 1:
                current_end = max(current_end, next_end)
            else:
                merged.append([current_start, current_end])
                current_start, current_end = next_start, next_end
        merged.append([current_start, current_end])

        result = []
        for start, end in merged:
            if end < filter_start or start > filter_end:
                result.append([start, end])
            elif filter_start <= start and end <= filter_end:
                continue
            elif start < filter_start and end > filter_end:
                result.append([start, filter_start - 1])
                result.append([filter_end + 1, end])
            elif start < filter_start:
                result.append([start, filter_start - 1])
            else:
                result.append([filter_end + 1, end])
        return result
