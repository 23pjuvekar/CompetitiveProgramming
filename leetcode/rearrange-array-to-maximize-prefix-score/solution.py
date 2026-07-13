class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        n = []
        total = 0
        res = 0
        p = []
        zero = 0
        for num in nums:
            if num > 0:
                p.append(num)
                total += num
                res += 1
            elif num == 0:
                zero += 1
            else:
                n.append(num)
        if total > 0:
            res += zero
        n.sort(reverse=True)
        for i in range(len(n)):
            total += n[i]
            if total > 0:
                res += 1
        return res
