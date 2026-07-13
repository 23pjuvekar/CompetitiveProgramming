class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

        same = -1
        for i in range(min(len(s1), len(s2), len(s3))):
            if s1[i] == s2[i] == s3[i]:
                same = i
            else:
                break
        
        if same == -1:
            return -1
        
        return len(s1) + len(s2) + len(s3) - (3 * (same + 1))
