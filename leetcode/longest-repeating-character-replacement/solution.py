class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        res = 0
        word_count = {}

        l = 0
        for r in range(len(s)):
            word_count[s[r]] = 1 + word_count.get(s[r], 0)
            length = max(word_count.values())
            while (r - l + 1 > k + length):
                word_count[s[l]] -= 1
                l += 1
                length = max(word_count.values())
            res = max(r - l + 1, res)
        
        return res
