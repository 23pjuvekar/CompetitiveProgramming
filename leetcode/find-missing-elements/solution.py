class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        max_num = max(nums)
        min_num = min(nums)
        nums_set = set(nums)
        res = []
        
        for number in range(min_num, max_num + 1):
            if number not in nums_set:
                res.append(number)
        return res
