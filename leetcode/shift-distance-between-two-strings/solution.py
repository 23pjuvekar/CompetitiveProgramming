class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        
        total_distance = 0

        for char_s, char_t in zip(s, t):
            start = ord(char_s) - ord('a')
            target = ord(char_t) - ord('a')
            
            fwd_cost = 0
            curr = start
            while curr != target:
                fwd_cost += nextCost[curr]
                curr = (curr + 1) % 26
                
            bwd_cost = 0
            curr = start
            while curr != target:
                bwd_cost += previousCost[curr]
                curr = (curr - 1) % 26
                
            total_distance += min(fwd_cost, bwd_cost)
            
        return total_distance
