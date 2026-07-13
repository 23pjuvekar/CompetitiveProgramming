class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
     a = 0
     j = len(nums)
     c = nums.count(0)

     for i in range(j):
         if nums[i] == 0 and i < j - c:
             a += 1
     return a
