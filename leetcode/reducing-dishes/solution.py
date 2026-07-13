class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        

        satisfaction.sort()
        positive_sum = 0
        curr_res = 0
        res = 0
        positive_count = 0

        first_non_neg = float("inf")
        for i in range(len(satisfaction)):
            if satisfaction[i] >= 0:
                positive_count += 1
                positive_sum += satisfaction[i]
                curr_res += satisfaction[i] * positive_count
            res = max(res, curr_res)
        
        for i in range(len(satisfaction) - 1, -1, -1):
            if satisfaction[i] < 0:
                positive_sum += satisfaction[i]
                curr_res += positive_sum
            res = max(res, curr_res)
        return res
