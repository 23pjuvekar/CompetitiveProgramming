class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        tracker_a = set()
        tracker_b = set()
        same_a = set()
        res = []

        for i in range(len(A)):
            tracker_a.add(A[i])
            tracker_b.add(B[i])

            if A[i] not in same_a and (A[i] in tracker_a and A[i] in tracker_b):
                same_a.add(A[i])
            
            if B[i] not in same_a and (B[i] in tracker_a and B[i] in tracker_b):
                same_a.add(B[i])
            
            res.append(len(same_a))
        
        return res
