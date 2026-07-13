class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return not ord(coordinates[0]) % 2 == int(coordinates[1]) % 2
