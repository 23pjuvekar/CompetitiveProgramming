class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        nums2 = list(nums)
        nums2.sort()
        curr = -1
        for n1, n2 in zip(nums, nums2):
            if n1 != n2:
                if curr == -1:
                    curr = n1
                else:
                    curr = curr & n1
        if curr == -1:
            return 0
        return curr
