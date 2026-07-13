class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        m = 0
        res = -1
        cnt = 0
        dp = []
        for b, d in logs:
            dp.append([b, 1])
            dp.append([d, -1])
        dp.sort()
        for d, i in dp:
            cnt += i
            if cnt > m:
                m = cnt
                res = d
        return res
