class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        max_res = nums[0]
        max_amount = 0

        for n in nums:
            if n == max_res:
                max_amount += 1
            else:
                if max_amount == 0:
                    max_amount += 1
                    max_res = n
                else:
                    max_amount -= 1
        
        return max_res
