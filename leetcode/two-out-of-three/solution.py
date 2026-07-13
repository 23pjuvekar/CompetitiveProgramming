class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        n1 = set(nums1)
        n2 = set(nums2)
        n3 = set(nums3)
        ntotal = n1 | n2 | n3
        res = []
        for n in ntotal:
            curr = 0
            if n in n1:
                curr += 1
            if n in n2:
                curr += 1
            if n in n3:
                curr += 1
            if curr > 1:
                res.append(n)
        return res
