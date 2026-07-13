class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:


        boxTypes.sort(reverse=True, key=lambda x: x[1])
        
        space_left = truckSize
        res = 0
        for box in boxTypes:
            if space_left > box[0]:
                space_left -= box[0]
                res += box[0] * box[1]
            else:
                res += space_left * box[1]
                space_left = 0

        return res
