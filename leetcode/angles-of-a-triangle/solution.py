class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:

        sides.sort()
        a, b, c = sides
        if a + b <= c:
            return []
        
        angle_a = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_b = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_c = degrees(acos((a**2 + b**2 - c**2) / (2 * a * b)))
        
        result = [angle_a, angle_b, angle_c]
        result.sort()
        return result
