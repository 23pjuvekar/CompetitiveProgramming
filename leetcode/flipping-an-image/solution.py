class Solution:
    def flipAndInvertImage(self, A):
        return [[1 ^ i for i in reversed(row)] for row in A]
