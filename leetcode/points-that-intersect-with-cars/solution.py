class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        nums.sort()
        dp = []

        for num in nums:
            if len(dp) == 0:
                dp.append(num)
            else:
                if dp[-1][1] >= num[0]:
                    dp[-1][1] = max(dp[-1][1], num[1])
                else:
                    dp.append(num)
        print(dp)
        res = 0
        for d in dp:
            res += d[1] - d[0] + 1
        return res
