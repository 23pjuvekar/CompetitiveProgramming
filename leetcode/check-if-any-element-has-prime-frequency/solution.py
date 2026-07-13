class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isPrime(nums):
            if nums == 1:
                return False
            for i in range(2, int(nums ** 0.5) + 1):
                if nums % i == 0:
                    return False
            return True

        for key, val in Counter(nums).items():
            if isPrime(val):
                return True
        return False
