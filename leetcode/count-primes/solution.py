class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        arr = [True] * n
        arr[0] = arr[1] = False  # 0 and 1 are not primes

        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(2 * i, n, i):  # start from i*i
                    arr[j] = False

        return sum(arr)
