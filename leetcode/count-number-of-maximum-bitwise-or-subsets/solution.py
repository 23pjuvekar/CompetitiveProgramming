class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        for num in nums:
            k = k | num
        res = 0
        def bt(curr, i):
            if i == n:
                return 1 if curr == k else 0
            return bt(curr, i + 1) + bt(curr | nums[i], i + 1)
        return bt(0, 0)
