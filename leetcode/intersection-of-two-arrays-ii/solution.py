class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1 = Counter(nums1)
        res = []

        for ite in nums2:
            if ite not in c1:
                continue
            else:
                if c1[ite] == 0:
                    continue
                else:
                    res.append(ite)
                    c1[ite] -= 1
        
        return res
