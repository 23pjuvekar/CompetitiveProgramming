class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        min_c = 1
        max_c = len(nums)
        set_nums = set(nums)

        res = []

        for num in range(min_c, max_c + 1):
            if num not in set_nums:
                res.append(num)

        return res
