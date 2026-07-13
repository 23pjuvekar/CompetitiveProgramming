class Solution:
    def isGood(self, nums: List[int]) -> bool:

        m = 0
        m_c = 1
        seen = set()
        for n in nums:
            seen.add(n)
            if m == n:
                m_c += 1
            elif n > m:
                m = max(m, n)
                m_c = 1
        
        return len(seen) == m and len(nums) == m + 1 and m_c == 2
