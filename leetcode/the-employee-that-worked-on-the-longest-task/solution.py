class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:

        last = 0
        res = 0
        length_m = 0

        for i, t in logs:
            if length_m == t - last:
                res = min(res, i)
            elif length_m < t - last:
                res = i
                length_m = t - last
            last = t
        return res
