class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        alphabet_array = [0] * 26

        for i in range(len(s)):
            alphabet_array[ord("a") - ord(s[i])] += i
            alphabet_array[ord("a") - ord(t[i])] -= i

        res = 0
        for i in range(26):
            res += abs(alphabet_array[i])
        return res
