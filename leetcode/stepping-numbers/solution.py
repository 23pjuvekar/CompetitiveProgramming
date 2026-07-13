class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:

        res = set()
        def dfs(curr):
            if curr > high:
                return
            if curr >= low:
                res.add(curr)
            last_digit = curr % 10
            if last_digit < 9:
                nxt = curr * 10 + (last_digit + 1)
                dfs(nxt)
            if last_digit > 0:
                nxt = curr * 10 + (last_digit - 1)
                dfs(nxt)

        if low == 0:
            res.add(0)
            
        for i in range(1, 10):
            dfs(i)
            
        return sorted(list(res))
