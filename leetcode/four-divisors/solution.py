class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        res = 0
        for num in nums:
            total = 0
            amt = 0
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    total += 1
                    amt += i 
                    if num // i != i:
                        amt += num // i 
                        total += 1
                    if total > 4:
                        break
            print(total, amt)
            if total == 4:
                res += amt
        return res
