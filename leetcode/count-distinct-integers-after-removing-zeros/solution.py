class Solution:
    def countDistinct(self, n: int) -> int:

        s_n = str(n)
        length = len(s_n)

        memo = {}

        def solve(idx, tight, is_started):
            if idx == length:
                return 1 if is_started else 0

            state = (idx, tight, is_started)
            if state in memo:
                return memo[state]

            ans = 0
            upper_bound = int(s_n[idx]) if tight else 9

            for digit in range(upper_bound + 1):
                if not is_started and digit == 0:
                    ans += solve(idx + 1, tight and (digit == upper_bound), False)
                elif digit == 0:
                    continue
                else:
                    ans += solve(idx + 1, tight and (digit == upper_bound), True)
            memo[state] = ans
            return ans
                    
        return solve(0, True, False)
