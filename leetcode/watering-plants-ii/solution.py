class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        A = capacityA
        B = capacityB
        l = 0
        r = len(plants) - 1
        refills = 0
        while l < r:
            if capacityA < plants[l]:
                refills += 1
                capacityA = A
            capacityA -= plants[l]
            plants[l] = 0
            l += 1
            if capacityB < plants[r]:
                refills += 1
                capacityB = B
            capacityB -= plants[r]
            plants[r] = 0
            r -= 1
        if plants[l] > max(capacityA, capacityB):
            refills += 1
        return refills
