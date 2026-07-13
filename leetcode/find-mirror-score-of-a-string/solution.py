from collections import defaultdict

class Solution:
    def calculateScore(self, s: str) -> int:
        tracker = defaultdict(list)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        m_m = {char: alphabet[::-1][i] for i, char in enumerate(alphabet)}

        res = 0
        marked = set()
        
        for i in range(len(s)):
            if i in marked:
                continue

            if s[i] in m_m and m_m[s[i]] in tracker:
                while tracker[m_m[s[i]]]:
                    j = tracker[m_m[s[i]]].pop()
                    if j not in marked:
                        res += (i - j)
                        marked.add(i)
                        marked.add(j)
                        break
            
            tracker[s[i]].append(i)

        return res
