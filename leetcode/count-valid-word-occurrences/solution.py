class Solution:
    def isLow(self, ch):
        return 'a' <= ch <= 'z'

    def countWordOccurrences(self, chunks, queries):
        mp = {}
        curr = ""
        s = "".join(chunks)
        n = len(s)

        for i in range(n):
            ch = s[i]
            if self.isLow(ch):
                curr += ch
            elif ch == '-':
                if len(curr) != 0 and i + 1 < n and self.isLow(s[i + 1]):
                    curr += '-'
                else:
                    if len(curr) != 0:
                        mp[curr] = mp.get(curr, 0) + 1
                        curr = ""
            else:
                if len(curr) != 0:
                    mp[curr] = mp.get(curr, 0) + 1
                    curr = ""

        if len(curr) != 0:
            mp[curr] = mp.get(curr, 0) + 1

        ans = []
        for str_ in queries:
            ans.append(mp.get(str_, 0))
        return ans
