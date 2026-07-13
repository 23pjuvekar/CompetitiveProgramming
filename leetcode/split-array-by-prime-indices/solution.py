class Solution:
    def splitArray(self, nums: List[int]) -> int:

        def isPrime(number):
            if number < 2:
                return False
            for d in range(2, int(number ** 0.5) + 1):
                if number % d == 0:
                    return False
            return True
        
        res = 0
        for i in range(len(nums)):
            if isPrime(i) == True:
                res += nums[i]
            else:
                res -= nums[i]
        return abs(res)
