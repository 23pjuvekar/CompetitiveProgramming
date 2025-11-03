class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        stack = []
        res = 0
        for i in range(len(colors)):
            if stack and stack[-1][0] == colors[i]:
                res += min(stack[-1][1], neededTime[i])
                stack[-1][1] = max(stack[-1][1], neededTime[i])
            else:
                stack.append([colors[i], neededTime[i]])
        return res

