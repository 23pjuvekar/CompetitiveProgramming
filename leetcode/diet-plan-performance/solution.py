class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        

        l = 0
        total = 0
        res = 0
        for r in range(len(calories)):
            total += calories[r]
            if r - l + 1 > k:
                total -= calories[l]
                l += 1 
            if r - l + 1 == k and total > upper:
                res += 1
            if r - l + 1 == k and total < lower:
                res -= 1
        return res
