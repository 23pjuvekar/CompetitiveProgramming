class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = []
        p = []

        for num in nums:
            if num < 0:
                n.append(num)
            else:
                p.append(num)
        oi = 0
        ei = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = p[oi]
                oi += 1
            else:
                nums[i] = n[ei]
                ei += 1
        return nums
