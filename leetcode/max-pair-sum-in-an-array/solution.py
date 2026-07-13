class Solution:
    def maxSum(self, nums: List[int]) -> int:

        c1 = defaultdict(list)
        for num in nums:
            n = num
            m = num % 10
            while num:
                m = max(m, num % 10)
                num = num // 10
            heappush(c1[m], -n)

        res = -1
        for key, l in c1.items():
            c = 0
            if len(l) > 1:
                c += -heappop(l)
                c += -heappop(l)
                res = max(c, res)
        return res
