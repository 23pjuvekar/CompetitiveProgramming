class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        0, 1
        0 1 1 --> 011, 3
        011 1 001 --> 0111001, 7
        0111001 1 0110001 --> 011100110110001, 15 = 2^4 - 1 = 2^n - 1
        """

        if n == 1:
            return "0"
        
        length = 2 ** n

        if k < length // 2:
            return self.findKthBit(n - 1, k)
        elif k == length // 2:
            return "1"
        else:
            opposite_bit = self.findKthBit(n - 1, length - k)
            return "1" if opposite_bit == "0" else "0"
