class Solution:
    def earliestFinishTime(self,landStartTime: List[int],landDuration: List[int],waterStartTime: List[int],waterDuration: List[int]) -> int:
        res = float('inf')
        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):
            a, d = landStartTime[i], landDuration[i]
            for j in range(m):
                b, e = waterStartTime[j], waterDuration[j]
                land_end = a + d
                start_water = max(land_end, b)
                finish1 = start_water + e
                water_end = b + e
                start_land = max(water_end, a)
                finish2 = start_land + d
                res = min(res, finish1, finish2)
        return res
