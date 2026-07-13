class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        prev_s, prev_e = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            curr_s, curr_e = intervals[i]
            if curr_s <= prev_e:
                prev_e = max(curr_e, prev_e)
            else:
                res.append([prev_s, prev_e])
                prev_s = curr_s
                prev_e = curr_e

        res.append([prev_s, prev_e])
        return res
