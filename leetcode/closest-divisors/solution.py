class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        def get_factors(target):
            for i in range(int(math.sqrt(target)), 0, -1):
                if target % i == 0:
                    return [i, target // i]
            return [float("inf"), float("-inf")]

        factors1 = get_factors(num + 1)
        factors2 = get_factors(num + 2)
        diff1 = abs(factors1[0] - factors1[1])
        diff2 = abs(factors2[0] - factors2[1])

        return factors1 if diff1 < diff2 else factors2
