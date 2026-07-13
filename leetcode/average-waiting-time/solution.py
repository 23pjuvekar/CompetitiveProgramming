class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        res = 0

        for customer in customers:
            if time < customer[0]:
                time = customer[0] + customer[1]
            else:
                time += customer[1]
            
            res += time - customer[0]
        
        return res / len(customers)
