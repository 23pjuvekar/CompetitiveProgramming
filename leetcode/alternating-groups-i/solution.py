class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        colors.extend(colors[0:2])
        count = 0
        
        for i in range(len(colors)-2):
            if colors[i] != colors[i+1] and colors[i+1] != colors[i+2]:
                count += 1
                
        return count
