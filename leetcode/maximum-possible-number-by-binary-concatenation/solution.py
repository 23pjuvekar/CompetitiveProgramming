class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:

        n1, n2, n3 = nums
        b1, b2, b3 = n1.bit_length(),n2.bit_length(), n3.bit_length()     
        
        return max(                                                      
                (n1 <<(b2+b3)) + (n2 <<b3) + n3, (n1 <<(b3+b2)) + (n3 <<b2) + n2,
                (n2 <<(b1+b3)) + (n1 <<b3) + n3, (n2 <<(b3+b1)) + (n3 <<b1) + n1,
                (n3 <<(b1+b2)) + (n1 <<b2) + n2, (n3 <<(b2+b1)) + (n2 <<b1) + n1
                )
