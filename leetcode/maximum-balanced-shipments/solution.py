class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:

        res = 0
        curr_max = float("-inf")
        for i in range(len(weight)):
            curr_max = max(curr_max, weight[i])
            if weight[i] < curr_max:
                res += 1
                curr_max = float("-inf")
        return res
