class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        travel_days = set(days)

        for day in range(1, days[-1] + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                one_day = dp[max(0, day - 1)] + costs[0]
                seven_day = dp[max(0, day - 7)] + costs[1]
                thirty_day = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(one_day, seven_day, thirty_day)
            
        return dp[days[-1]]
