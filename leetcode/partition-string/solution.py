class Solution:
    def partitionString(self, s: str) -> List[str]:

        st = set()
        res = []
        l = 0
        for r in range(len(s)):
            if s[l:r+1] in st:
                continue
            else:
                st.add(s[l:r+1])
                res.append(s[l:r+1])
                l = r + 1
        return res
