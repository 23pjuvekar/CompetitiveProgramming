class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_tracker = {}

        for i in range(len(nums2)):
            map_tracker[nums2[i]] = i

        res = []

        for num in nums1:
            skip = -1
            i = map_tracker[num] + 1
            while i < len(nums2):
                if nums2[i] > num:
                    res.append(nums2[i])
                    skip = 1
                    break
                i += 1
            if skip == -1:
                res.append(-1)
            
        return res
