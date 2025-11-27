class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        res = float("-inf")
        for i in range(k):
            start = i
            for j in range(start + (k - 1), len(nums), k):
                # print(start, j+1)
                array_total = prefix[j + 1] - prefix[start]
                res = max(res, array_total)
                if array_total < 0:
                    start = j + 1
        return res
                