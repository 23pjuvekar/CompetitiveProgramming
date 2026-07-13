class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        odd_1 = []
        even_1 = []
        odd_2 = []
        even_2 = []
        for i in range(len(s1)):
            if i % 2 == 0:
                even_1.append(s1[i])
                even_2.append(s2[i])
            else:
                odd_1.append(s1[i])
                odd_2.append(s2[i])
        even_1.sort()
        even_2.sort()
        odd_1.sort()
        odd_2.sort()
        return even_1 == even_2 and odd_1 == odd_2
