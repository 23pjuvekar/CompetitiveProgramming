class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        timeslots = []
        for s in slots1:
            if s[1] - s[0] >= duration:
                timeslots.append(s)
        for s in slots2:
            if s[1] - s[0] >= duration:
                timeslots.append(s)
        combined = []

        for slot in timeslots:
            combined.append([slot[0], 1])
            combined.append([slot[1], -1])
        combined.sort()

        count = 0
        for i in range(len(combined) - 1):
            time, val = combined[i]
            count += val
            if count == 2 and combined[i+1][0] >= time + duration:
                return [time, time + duration]
        return []
