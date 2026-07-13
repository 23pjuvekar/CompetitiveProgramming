class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        print(points)
        n = len(points)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if y2 <= y1 and x1 <= x2:
                    is_valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            is_valid = False
                            break
                    if is_valid:
                        count += 1
        return count
