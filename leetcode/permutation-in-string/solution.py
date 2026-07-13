class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s2) < len(s1):
            return False

        # Put s1 into array form
        searchString = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            searchString[ord(s1[i]) - ord("a")] += 1
            window[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if searchString[i] == window[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            window[index] += 1
            if window[index] - 1 == searchString[index]:
                matches -= 1
            elif window[index] == searchString[index]:
                matches += 1

            index = ord(s2[l]) - ord("a")
            window[index] -= 1
            if window[index] + 1 == searchString[index]:
                matches -= 1
            elif window[index] == searchString[index]:
                matches += 1

            l += 1
            
        return matches == 26
