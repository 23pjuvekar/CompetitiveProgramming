class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        res = [256, 0, 0, 0, 0]
        max_count = 0
        total_count = 0
        for i in range(0, 256):
            if count[i] != 0:
                res[0] = min(res[0], i)
                res[1] = max(res[1], i)
            if count[i] > max_count:
                res[4] = i
                max_count = count[i]
            res[2] += count[i] * i
            total_count += count[i]
        res[2] = res[2] / total_count
        n = total_count
        def get_val(target):
            curr = 0
            for i in range(256):
                curr += count[i]
                if curr >= target:
                    return i
            return 0
        if n % 2 == 1:
            res[3] = float(get_val(n // 2 + 1))
        else:
            m1 = get_val(n // 2)
            m2 = get_val(n // 2 + 1)
            res[3] = (m1 + m2) / 2.0
            
        return res
