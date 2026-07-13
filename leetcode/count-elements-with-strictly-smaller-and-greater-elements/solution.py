class Solution:
    def countElements(self, nums: List[int]) -> int:

        count = Counter(nums)
        res = len(nums) - count[min(nums)] - count[max(nums)]
        if res > -1:
            return res
        return 0
