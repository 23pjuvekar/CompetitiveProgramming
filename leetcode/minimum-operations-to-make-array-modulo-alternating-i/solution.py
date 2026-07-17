class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def cost_for_target(values, target, modulus):
            total_cost = 0
            for value in values:
                remainder = value % modulus
                distance = abs(remainder - target)
                total_cost += min(distance, modulus - distance)
            return total_cost

        even_values = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        odd_values = [nums[i] for i in range(len(nums)) if i % 2 == 1]

        even_costs = [cost_for_target(even_values, target, k) for target in range(k)]
        odd_costs = [cost_for_target(odd_values, target, k) for target in range(k)]

        best_odd_cost = float('inf')
        second_best_odd_cost = float('inf')
        best_odd_target = -1

        for target in range(k):
            if odd_costs[target] < best_odd_cost:
                second_best_odd_cost = best_odd_cost
                best_odd_cost = odd_costs[target]
                best_odd_target = target
            elif odd_costs[target] < second_best_odd_cost:
                second_best_odd_cost = odd_costs[target]

        min_total_cost = float('inf')

        for even_target in range(k):
            # even and odd targets must differ, so skip the odd target
            # that matches even_target and fall back to the next best
            odd_cost_excluding_even_target = (
                second_best_odd_cost if even_target == best_odd_target else best_odd_cost
            )
            total_cost = even_costs[even_target] + odd_cost_excluding_even_target
            min_total_cost = min(min_total_cost, total_cost)

        return min_total_cost
