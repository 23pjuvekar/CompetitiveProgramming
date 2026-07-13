class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        res = 0
        distance = float("inf")
        for i in range(n):
            res += abs(nums1[i] - nums2[i])
            distance = min(abs(nums1[i] - nums2[-1]), distance, abs(nums2[i] - nums2[-1]))
            if nums1[i] <= nums2[-1] <= nums2[i] or nums2[i] <= nums2[-1] <= nums1[i]:
                distance = 0
        res += distance
        return res + 1
