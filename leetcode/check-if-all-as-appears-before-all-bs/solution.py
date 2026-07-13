class Solution:
    def checkString(self, s: str) -> bool:

        b_seen = False

        for c in s:
            if c == "b":
                b_seen = True
            if b_seen and c == "a":
                return False
        return True
