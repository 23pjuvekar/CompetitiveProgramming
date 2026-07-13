class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        diff = [0] * (n + 1)

        for position, bulb_range in enumerate(lights):
            if bulb_range > 0:
                left = max(0, position - bulb_range)
                right = min(n - 1, position + bulb_range)
                diff[left] += 1
                diff[right + 1] -= 1

        coverage = [0] * n
        running_sum = 0

        for i in range(n):
            running_sum += diff[i]
            coverage[i] = running_sum

        extra_bulbs = 0
        i = 0

        while i < n:
            if coverage[i] > 0:
                i += 1
            else:
                extra_bulbs += 1
                i += 3

        return extra_bulbs
