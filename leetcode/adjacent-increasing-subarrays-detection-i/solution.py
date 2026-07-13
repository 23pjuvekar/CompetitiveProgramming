class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        f_p = 0
        s_p = k
        length = 1

        while s_p < len(nums):
            if f_p != 0 and nums[f_p - 1] < nums[f_p] and nums[s_p - 1] < nums[s_p]:
                length += 1
            else:
                length = 1
                
            if length == k:
                return True

            f_p += 1
            s_p += 1

        return False
