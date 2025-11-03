class Solution:
    def canWin(self, currentState: str) -> bool:

        memo = {}

        def solve(s):
            if s in memo:
                return memo[s]
            
            for i in range(len(s) - 1):
                if s[i:i+2] == "++":
                    temp_list = list(s)
                    temp_list[i] = "-"
                    temp_list[i+1] = "-"
                    if not solve("".join(temp_list)):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        
        return solve(currentState)