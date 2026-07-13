class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        Bulky = False
        Heavy = False

        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4  or length * width * height >= 10 ** 9:
            Bulky = True
        
        if mass >= 100:
            Heavy = True

        if Bulky and Heavy:
            return "Both"
        elif Bulky:
            return "Bulky"
        elif Heavy:
            return "Heavy" 
        else:
            return "Neither"
