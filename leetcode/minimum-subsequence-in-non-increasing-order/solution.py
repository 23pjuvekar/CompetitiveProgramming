class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        h = []
        heapify(h)
        total = 0
        for num in nums:
            total += num
            heappush(h, -num)

        sub_total = 0
        res = []
        while total >= sub_total:
            val = -heappop(h)
            total -= val
            sub_total += val
            res.append(val)
        return res
