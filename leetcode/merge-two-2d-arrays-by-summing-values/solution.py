class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        c1 = defaultdict(int)
        res = []
        for ids, val in nums1:
            c1[ids] += val
        for ids, val in nums2:
            c1[ids] += val
        for key, val in c1.items():
            res.append([key, val])
        res.sort()
        return res
