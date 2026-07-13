class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        y_d = (coordinates[1][1] - coordinates[0][1]) 
        x_d = (coordinates[1][0] - coordinates[0][0])
        if x_d != 0:
            slope_t = y_d / x_d
        else:
            slope_t = float("inf")

        for i in range(len(coordinates) - 1):
            y_d = (coordinates[i+1][1] - coordinates[i][1]) 
            x_d = (coordinates[i+1][0] - coordinates[i][0])
            if x_d != 0:
                slope = y_d / x_d
            else:
                slope = float("inf")
            if slope != slope_t:
                return False
        return True
