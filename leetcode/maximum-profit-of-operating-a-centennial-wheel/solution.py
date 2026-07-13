class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:

        max_profit = -1
        best_rotation = -1
        
        current_profit = 0
        waiting_customers = 0
        rotation = 0
        
        i = 0
        n = len(customers)
        
        while i < n or waiting_customers > 0:
            rotation += 1
            
            if i < n:
                waiting_customers += customers[i]
                i += 1
            
            boarding = min(4, waiting_customers)
            waiting_customers -= boarding
            
            current_profit += (boarding * boardingCost) - runningCost
            
            if current_profit > max_profit and current_profit > 0:
                max_profit = current_profit
                best_rotation = rotation
                
        return best_rotation
