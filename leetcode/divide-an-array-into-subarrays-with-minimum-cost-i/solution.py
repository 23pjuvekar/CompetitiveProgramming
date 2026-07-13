class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        m_1 = float("inf") 
        m_2 = float("inf") - 1
        m_3 = float("inf") - 2
        for i in range(1, len(nums)):
            if nums[i] < m_1:
                m_3 = m_2
                m_2 = m_1
                m_1 = nums[i]
            elif nums[i] < m_2:
                m_3 = m_2
                m_2 = nums[i]
            elif nums[i] < m_3:
                m_3 = nums[i]

        return m_1 + m_2 + nums[0]
