class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 = set(nums1)
        n2 = set(nums2)

        res = [0, 0]
        for num in nums1:
            if num in n2:
                res[0] += 1
        for num in nums2:
            if num in n1:
                res[1] += 1
        return res
