class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:

        res = -1
        for index in range(len(sensor1)):
            if sensor1[index] != sensor2[index]:
                res = index
                break
        
        if res == -1 or res + 1 == len(sensor1):
            return -1
        
        if sensor1[index:len(sensor1) - 1] == sensor2[index+1:] and sensor2[index:len(sensor1) - 1] == sensor1[index+1:]:
            return -1

        if sensor1[index:len(sensor1) - 1] == sensor2[index+1:]:
            return 1
        elif sensor2[index:len(sensor1) - 1] == sensor1[index+1:]:
            return 2
