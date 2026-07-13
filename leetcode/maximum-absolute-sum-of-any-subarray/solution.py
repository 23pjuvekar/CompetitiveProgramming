class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        m_p = 0
        m_n = 0
        curr_p = 0
        curr_n = 0
        for num in nums:
            if num < 0:
                curr_n += num
                curr_p += num
                curr_p = max(curr_p, 0)
                m_n = min(m_n, curr_n)
            elif num > 0:
                curr_n += num
                curr_p += num
                curr_n = min(curr_n, 0)
                m_p = max(m_p, curr_p)
        return max(abs(m_p), abs(m_n))
