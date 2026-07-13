class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(int(str(nums[i])[0]), nums[j] % 10) == 1:
                    res += 1
        return res
