class Solution:
    def numWays(self, s: str) -> int:

        total = 0
        for c in s:
            total += int(c)
        
        if total % 3 != 0:
            return 0
        
        if total == 0:
            return (((len(s) - 1) * (len(s) - 2)) // 2 ) % (10 ** 9 + 7)
        
        count = 0
        dp = [0, 0]
        for c in s:
            if c == "1":
                count += 1
            if count == int(total / 3) and c == "0":
                dp[0] += 1
            if count == int(2 * total / 3) and c == "0":
                dp[1] += 1
        
        return ((dp[0] + 1) * (dp[1] + 1)) % (10 ** 9 + 7)
