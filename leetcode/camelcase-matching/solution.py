class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def isMatch(query, pattern):
            i = 0
            for char in query:
                if i < len(pattern) and char == pattern[i]:
                    i += 1
                elif char.isupper():
                    return False
            return i == len(pattern)
        
        return [isMatch(q, pattern) for q in queries]
