class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_length = 0
        curr = 0

        for c in s:
            if c == " ":
                if curr != 0:
                    last_length = curr
                curr = 0
            else:
                curr += 1

        if curr != 0:
            return curr

        return last_length
