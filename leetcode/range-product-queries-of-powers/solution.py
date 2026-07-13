class Solution:
    def productQueries(self, num: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []
        current_power = 1
        while num > 0:
            if num % 2 == 1:
                powers.append(current_power)
            num //= 2
            current_power *= 2

        n = len(powers)
        product = [[0] * n for _ in range(n)]
        for start in range(n):
            product[start][start] = powers[start]
            for end in range(start + 1, n):
                product[start][end] = product[start][end - 1] * powers[end] % MOD

        return [product[left][right] for left, right in queries]
