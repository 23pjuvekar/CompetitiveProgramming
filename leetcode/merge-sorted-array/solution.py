class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        c_p = len(nums1) - 1
        m_p = m - 1
        n_p = n - 1

        while n_p != -1:
            if m_p != -1 and nums1[m_p] > nums2[n_p]:
                nums1[c_p] = nums1[m_p]
                m_p -= 1
            else:
                nums1[c_p] = nums2[n_p]
                n_p -= 1
            c_p -= 1
