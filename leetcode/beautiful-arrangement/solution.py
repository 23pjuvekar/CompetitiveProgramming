class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.back_track(n, 1, set())
        return self.count
        
    def back_track(self, N, idx, temp):
        if len(temp) == N:
            self.count += 1
            return
            
        for i in range(1, N+1):
            if i not in temp and (i % idx == 0 or idx % i == 0):
                temp.add(i)
                self.back_track(N, idx+1, temp)
                temp.remove(i)
