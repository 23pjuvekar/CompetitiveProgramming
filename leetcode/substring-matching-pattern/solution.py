class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p_a = p.split("*")
        g1 = (p_a[0] == "")
        g2 = (p_a[1] == "")
        start = 0
        for i in range(start, len(s) - len(p_a[0]) + 1):
            if s[i:i + len(p_a[0])] == p_a[0]:
                start = i + len(p_a[0])
                g1 = True
                break
        for i in range(start, len(s) - len(p_a[1]) + 1):
            if s[i:i + len(p_a[1])] == p_a[1]:
                start = i + len(p_a[1])
                g2 = True
                break
        return g1 and g2
