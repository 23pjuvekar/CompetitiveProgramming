class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def valid(x):
            matched = 0
            for num in nums1:
                if matched < len(nums2) and nums2[matched] - num == x:
                    matched += 1
            return matched == len(nums2)

        best = float('inf')
        for i in range(3):
            x = nums2[0] - nums1[i]
            if valid(x):
                best = min(best, x)
        return best
