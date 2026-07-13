class Solution:
    def minSwaps(self, data: List[int]) -> int:

        amount = sum(data)
        if amount == 0:
            return 0

        l, r = 0, 0
        ones = 0
        res = float("inf")

        while r < len(data):
            if data[r] == 1:
                ones += 1
            
            if r - l + 1 > amount:
                if data[l] == 1:
                    ones -= 1
                l += 1
                
            if r - l + 1 == amount:
                res = min(res, amount - ones)

            
            r += 1
        
        return res
