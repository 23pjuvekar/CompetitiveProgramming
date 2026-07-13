class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        co = Counter(s)
        prev = -1

        for key, val in co.items():
            if prev == -1:
                prev = val
            else:
                if prev != val:
                    return False
        return True
