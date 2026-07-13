class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        m1 = min(nums1)
        m2 = min(nums2)
        a = []
        for num in nums1:
            if num in nums2:
                a.append(num)
        if a:
            return min(a)

        if(m1>m2):
            return int(str(m2) + str(m1))
        else:
            return int(str(m1) + str(m2))
