# Backtracking

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []

        def bt(curr, start, total):
            if len(curr) == k and total == n:
                res.append(curr[:])  # Append a copy of curr
                return
            if len(curr) > k or total > n or start > 9:
                return
            
            # Include the current number
            curr.append(start)
            bt(curr, start + 1, total + start)
            curr.pop()
            
            # Skip the current number
            bt(curr, start + 1, total)

        bt([], 1, 0)
        return res
