class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        b1 = 0
        b2 = 0
        for i in range(1, 100):
            if i % 2 == 1:
                b1 += i
            else:
                b2 += i
            if (red >= b1 and blue >= b2) or (blue >= b1 and red >= b2):
                continue
            else:
                break
        return i - 1
