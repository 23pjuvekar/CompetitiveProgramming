class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def dnc(string):
            counter = Counter(string)

            for i in range(len(string)):
                if counter[string[i]] < k:
                    return max(dnc(string[:i]), dnc(string[i+1:]))
            
            return len(string)

        return dnc(s)
