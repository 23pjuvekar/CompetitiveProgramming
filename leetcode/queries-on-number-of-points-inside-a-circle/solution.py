class Solution:
        def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
                k = []
                count = 0 
                for i in queries:
                        x1 = i[0]
                        y1 = i[1]
                        r = i[2]
                        for j in points:
                                x2 = j[0]
                                y2 = j[1]
                                if (((x2 - x1)**2 + (y2 - y1)**2)**0.5) <= r :
                                        count = count + 1
                        k.append(count)
                        count = 0 
                return k
