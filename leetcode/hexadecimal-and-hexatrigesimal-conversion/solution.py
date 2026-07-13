class Solution:
    def concatHex36(self, n: int) -> str:
        digits36 = digits + ascii_uppercase
        hexDigs = hex(n*n)[2:]
        hextriDigs = ''
        n3 = n * n * n 
        while n3:
            n3, dig = divmod(n3, 36) 
            hextriDigs+= digits36[dig]

        return ''.join([hexDigs, hextriDigs[::-1]]).upper()
