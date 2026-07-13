class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        if finalSum % 2 != 0:
            return []
        result = []
        curr = 2
        while curr <= finalSum:
            result.append(curr)
            finalSum -= curr
            curr += 2
        result[-1] += finalSum
        return result
