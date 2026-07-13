class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapper = {}
        res = []

        for i in range(len(nums2)):
            mapper[nums2[i]] = i
        
        for i in range(len(nums1)):
            res.append(mapper[nums1[i]])
        
        return res
