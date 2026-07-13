class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        
        min_bulbs = math.ceil(brightness / 3)
        
        intervals.sort()
        
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        total_energy = 0
        for start, end in merged:
            duration = end - start + 1
            total_energy += min_bulbs * duration
        
        return total_energy
