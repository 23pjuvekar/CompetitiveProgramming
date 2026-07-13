class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)
        total_profit = sum(p * s for p, s in zip(prices, strategy))
        p_prefix = [0] * (n + 1)
        for i in range(n):
            p_prefix[i+1] = p_prefix[i] + prices[i]
            
        s_prefix = [0] * (n + 1)
        for i in range(n):
            s_prefix[i+1] = s_prefix[i] + (prices[i] * strategy[i])
            
        max_p = total_profit
        half_k = k // 2
        
        for j in range(n - k + 1):
            old_window_sum = s_prefix[j+k] - s_prefix[j]
            
            new_window_sum = p_prefix[j+k] - p_prefix[j+half_k]
            
            current_total = total_profit - old_window_sum + new_window_sum
            max_p = max(max_p, current_total)
            
        return max_p
