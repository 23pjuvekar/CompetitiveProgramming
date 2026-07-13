class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        even_count = sum(1 for x in nums if x % 2 == 0)
        odd_count = n - even_count

        if abs(even_count - odd_count) > 1:
            return -1

        def cost(start_parity):
            misplaced_even = []
            misplaced_odd = []

            for i, x in enumerate(nums):
                expected = (i + start_parity) % 2
                if x % 2 != expected:
                    if i % 2 == 0:
                        misplaced_even.append(i)
                    else:
                        misplaced_odd.append(i)

            if len(misplaced_even) != len(misplaced_odd):
                return float('inf')

            return sum(abs(a - b) for a, b in zip(misplaced_even, misplaced_odd))

        results = []
        results.append(cost(0))
        results.append(cost(1))

        return min(results)
