class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        h = []
        for num in nums:
            if h and h[-1] == num:
                continue
            h.append(num)
        
        res = 0
        for i in range(1, len(h) - 1):
            if(h[i-1] < h[i] > h[i+1]) or (h[i-1] > h[i] < h[i+1]):
                res += 1
        return res
