class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        startHours, startMinutes, startSeconds = map(int, startTime.split(":"))
        endHours, endMinutes, endSeconds = map(int, endTime.split(":"))

        startTotalSeconds = startHours * 3600 + startMinutes * 60 + startSeconds
        endTotalSeconds = endHours * 3600 + endMinutes * 60 + endSeconds

        elapsedSeconds = endTotalSeconds - startTotalSeconds
        

        return elapsedSeconds
