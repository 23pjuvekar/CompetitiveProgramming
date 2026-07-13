class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        c1 = Counter(tasks)
        print(c1)
        res = 0
        for key, val in c1.items():
            if val == 1:
                return -1
            res += (val // 6) * 2
            val = val % 6 
            if val == 1:
                res += 1
            res += (val // 2)
        return res
