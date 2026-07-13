class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        bucket = capacity
        res = 0
        for i in range(len(plants)):
            if plants[i] > bucket:
                bucket = capacity
                bucket -= plants[i]
                res += i
                res += (i + 1)
            else:
                bucket -= plants[i]
                res += 1
            print(i, res)
        return res
