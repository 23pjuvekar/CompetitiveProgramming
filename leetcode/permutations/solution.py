class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def back(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
                return
            for num in nums:
                if num not in comb:
                    comb.append(num)
                    back(comb)
                    comb.pop()

        back([])
        return res
