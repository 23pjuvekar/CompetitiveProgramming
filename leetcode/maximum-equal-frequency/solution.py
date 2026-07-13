class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = defaultdict(int)
        freq_count = defaultdict(int)
        max_freq = 0
        res = 0
        
        for i, num in enumerate(nums):
            if count[num] > 0:
                freq_count[count[num]] -= 1
                if freq_count[count[num]] == 0:
                    del freq_count[count[num]]
            count[num] += 1
            max_freq = max(max_freq, count[num])
            freq_count[count[num]] += 1
            if max_freq == 1:
                res = i + 1
            elif len(freq_count) == 1:
                if freq_count[max_freq] == 1:
                    res = i + 1
            elif len(freq_count) == 2:
                f1, f2 = freq_count.keys()
                if f1 > f2:
                    f1, f2 = f2, f1
                if f1 == 1 and freq_count[f1] == 1:
                    res = i + 1
                if f2 == f1 + 1 and freq_count[f2] == 1:
                    res = i + 1
                    
        return res
