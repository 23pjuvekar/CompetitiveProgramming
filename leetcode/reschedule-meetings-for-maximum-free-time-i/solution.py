class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        times = sorted(zip(startTime, endTime))
        gaps = [times[0][0]]
        for i in range(1, len(times)):
            gaps.append(times[i][0] - times[i-1][1])
        gaps.append(eventTime - times[-1][1])
        
        window_size = k + 1
        current_free_time = sum(gaps[:window_size])
        max_free_time = current_free_time
    
        for i in range(window_size, len(gaps)):
            current_free_time += gaps[i] - gaps[i - window_size]
            max_free_time = max(max_free_time, current_free_time)
        
        return max_free_time
