class Solution:
    def bestClosingTime(self, customers: str) -> int:

        Y = customers.count("Y")
        N = 0
        res = Y
        min_i = 0
        
        for i, char in enumerate(customers):
            if char == "Y":
                Y -= 1
            else:
                N += 1
            
            penalty = Y + N
            if penalty < res:
                res = penalty
                min_i = i + 1
                
        return min_i
