class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints.sort()
        res = float('inf')

        for index in range(1, len(timePoints)):
            time_one = int(timePoints[index-1][:2]) * 60 + int(timePoints[index-1][3:])
            time_two = int(timePoints[index][:2]) * 60 + int(timePoints[index][3:])
            diff = abs(time_two - time_one)
            res = min(res, diff)

        if len(timePoints) > 1:
            time_one = int(timePoints[0][:2]) * 60 + int(timePoints[0][3:])
            time_two = int(timePoints[len(timePoints)-1][:2]) * 60 + int(timePoints[len(timePoints)-1][3:])
            diff = 1440 - abs(time_two - time_one)
            res = min(res, diff)

        return res
