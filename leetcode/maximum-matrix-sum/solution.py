class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        total_sum = 0
        smallest_element = float("inf")
        negative_amt = 0
        for row in matrix:
            for element in row:
                total_sum += abs(element)
                smallest_element = min(smallest_element, abs(element))
                if element < 0:
                    negative_amt += 1

        if negative_amt % 2 == 1:
            return total_sum - 2 * smallest_element
        return total_sum
