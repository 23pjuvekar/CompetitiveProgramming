class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return False

        proper_divisor_sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                proper_divisor_sum += i
                if num // i != i: 
                    proper_divisor_sum += num // i

        return proper_divisor_sum == num
