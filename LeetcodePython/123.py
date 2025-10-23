class Solution(object):
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        length = len(prices)
        left_profits = [0] * length
        right_profits = [0] * (length + 1)

        left_min = prices[0]
        for i in range(1, length):
            left_profits[i] = max(left_profits[i - 1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

        right_max = prices[length - 1]
        for i in range(length - 2, -1, -1): 
            right_profits[i] = max(right_profits[i + 1], right_max - prices[i])
            right_max = max(right_max, prices[i])

        max_total_profit = 0
        for i in range(length):
            max_total_profit = max(max_total_profit, left_profits[i] + right_profits[i + 1])

        return max_total_profit