class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        seen = set()

        for val, amt in Counter(arr).items():
            if amt in seen:
                return False
            seen.add(amt)
        return True
