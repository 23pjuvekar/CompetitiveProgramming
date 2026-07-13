class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        n1 = set(nums1)
        res = float("inf")
        for num in nums2:
            if num in n1:
                res = min(res, num)
        if res == float("inf"):
            return -1
        return res
