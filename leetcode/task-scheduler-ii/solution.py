class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        next_available = {}
        res = 0
        for task in tasks:
            if task in next_available and res < next_available[task]:
                res = next_available[task]
            else:
                res += 1
            next_available[task] = res + space + 1
        return res
