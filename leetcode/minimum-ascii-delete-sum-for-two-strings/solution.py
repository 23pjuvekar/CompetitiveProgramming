class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = {}
        total_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)

        def max_common(i, j):
            if i >= len(s1) or j >= len(s2):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s1[i] == s2[j]:
                res = ord(s1[i]) + max_common(i + 1, j + 1)
            else:
                res = max(max_common(i, j + 1), max_common(i + 1, j))
            
            dp[(i, j)] = res
            return res
        
        return total_sum - 2 * max_common(0, 0)
