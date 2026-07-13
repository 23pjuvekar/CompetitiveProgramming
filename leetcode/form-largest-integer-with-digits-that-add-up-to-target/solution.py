class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        memo = {}
        def dp(remaining_target: int) -> str:
            if remaining_target == 0:
                return ""
            if remaining_target < 0:
                return "0"
            if remaining_target in memo:
                return memo[remaining_target]

            res = "0"
            for i in range(8, -1, -1):
                digit = str(i + 1)
                sub_res = dp(remaining_target - cost[i])
                if sub_res != "0":
                    candidate = digit + sub_res
                    if res == "0" or len(candidate) > len(res):
                        res = candidate
                    elif len(candidate) == len(res) and candidate > res:
                        res = candidate

            memo[remaining_target] = res
            return res

        result = dp(target)
        return result if result != "0" else "0"
