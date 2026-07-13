class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0
        prefix = 0
        result = 0
        for num in arr:
            prefix = (prefix + num) % 2
            if prefix == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1
        return result % MOD
