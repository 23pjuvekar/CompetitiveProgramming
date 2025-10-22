class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        Total_Length = len(nums1) + len(nums2)
        Half_Length = Total_Length // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1) - 1
        while True:
            nums1_index = (l + r) // 2
            nums2_index = (Half_Length - nums1_index) - 2

            nums1_left = nums1[nums1_index] if nums1_index >= 0 else float("-inf")
            nums1_right = nums1[nums1_index + 1] if (nums1_index + 1) < len(nums1) else float("inf")
            nums2_left = nums2[nums2_index] if nums2_index >= 0 else float("-inf")
            nums2_right = nums2[nums2_index + 1] if (nums2_index + 1) < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if Total_Length % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return min(nums1_right, nums2_right)
            elif nums1_left > nums2_right:
                r = nums1_index - 1
            else:
                l = nums1_index + 1



        