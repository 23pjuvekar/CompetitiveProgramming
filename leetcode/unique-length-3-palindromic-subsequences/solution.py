class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        tracker = defaultdict(list)

        for i in range(len(s)):
            tracker[s[i]].append(i)
        
        res = 0

        
        for char, indexs in tracker.items():
            if len(indexs) > 1:
                start = indexs[0]
                end = indexs[-1]
                uniq = set()
                for c in s[start+1:end]:
                    uniq.add(c)
                res += len(uniq)
        
        return res
