class Solution:
    def largestPalindromic(self, num: str) -> str:

        c = Counter(num)
        dp = []
        m_s = "-1"
        print(c)
        for k, v in c.items():
            dp.extend([k] * (v // 2))
            if v % 2 == 1:
                m_s = max(m_s, k)
        dp.sort(reverse=True)
        dp = "".join(dp)

        if dp and dp[0] == "0":
            dp = ""
        if m_s != "-1":
            return dp + m_s + dp[::-1]
        if not dp and m_s == "-1":
            return "0"
        return dp + dp[::-1]
