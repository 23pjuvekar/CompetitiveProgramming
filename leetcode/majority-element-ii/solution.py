class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        nums.sort()
        res = []
        n = len(nums)

        length = 0
        prev = -1
        for num in nums:
            if prev != num:
                if length > n // 3:
                    res.append(prev)
                prev = num
                length = 1
            else:
                length += 1
        
        if length > n // 3:
            res.append(prev)
        return res
