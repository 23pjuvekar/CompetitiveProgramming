class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        seen = set()
        n = len(s)
        for i in range(len(s)):
            c = s[i]
            if c not in seen:
                if i + distance[ord(c) - ord("a")] + 1 > n-1 or s[i + distance[ord(c) - ord("a")] + 1] != c:
                    print(c)
                    return False
            seen.add(c)
        return True
