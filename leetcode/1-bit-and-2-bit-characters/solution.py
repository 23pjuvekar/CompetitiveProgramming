class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            elif i == len(bits) - 1:
                return True
            else:
                i += 1
        return False
