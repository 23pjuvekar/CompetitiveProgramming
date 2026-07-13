class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        points = [1 if x == 1 else -1 for x in possible]
        total_sum = sum(points)
        alice_sum = 0

        for i in range(n - 1):
            alice_sum += points[i]
            bob_sum = total_sum - alice_sum
            if alice_sum > bob_sum:
                return i + 1
        return -1
