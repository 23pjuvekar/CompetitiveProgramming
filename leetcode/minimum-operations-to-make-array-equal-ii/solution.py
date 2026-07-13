class Solution:
    def minOperations(self, nums1, nums2, k):
        if k == 0:
            return 0 if nums1 == nums2 else -1

        total = 0
        operations = 0
        for value1, value2 in zip(nums1, nums2):
            difference = value1 - value2
            if difference % k != 0:
                return -1
            total += difference
            if difference > 0:
                operations += difference // k

        return operations if total == 0 else -1
