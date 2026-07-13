class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        n1 = set(nums1)
        n2 = set(nums2)
        seen1 = set()
        seen2 = set()
        res = [[], []]
        for num in nums1:
            if num not in n2 and num not in seen1:
                res[0].append(num)
                seen1.add(num)
        for num in nums2:
            if num not in n1 and num not in seen2:
                res[1].append(num)
                seen2.add(num)
        return res
