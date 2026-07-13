class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:

        limit = int(n**(1/3)) + 2 
        sums = defaultdict(int)
        ans = []
        
        for a in range(1, limit):
            a3 = a * a * a
            if a3 > n: 
                break
            for b in range(a, limit):
                val = a3 + (b * b * b)
                if val > n:
                    break
                count = sums[val]
                if count == 1:
                    ans.append(val)
                
                sums[val] += 1
                    
        return sorted(ans)
