class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        city_road_amt = defaultdict(int)
        for a, b in roads:
            city_road_amt[a] += 1
            city_road_amt[b] += 1
        
        list_road = [amt for city, amt in city_road_amt.items()]
        list_road.sort(reverse=True)

        res = 0
        print(list_road)
        for amt in list_road:
            res += amt * n
            n -= 1
        return res
