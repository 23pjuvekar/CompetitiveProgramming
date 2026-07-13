class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        c1 = defaultdict(list)
        for num in nums:
            curr = 0
            past = num
            while num:
                curr += num % 10
                num = num // 10
            c1[curr].append(past)
        
        res = -1
        for key, val in c1.items():
            if len(val) > 1:
                val.sort(reverse=True)
                res = max(val[0] + val[1], res)
        return res
