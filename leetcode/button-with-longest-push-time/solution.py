class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:

        prev = 0
        longest_index = 0
        longest_time = 0

        for index, (id, time) in enumerate(events):
            if index == 0:
                dur = time
            else:
                dur = time - prev

            if dur > longest_time or (dur == longest_time and id < longest_index):
                longest_time = dur
                longest_index = id

            prev = time

        return longest_index
