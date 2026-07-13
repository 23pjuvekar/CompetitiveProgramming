class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []

        for i in range(max_len):
            vertical = ''
            for word in words:
                if i < len(word):
                    vertical += word[i]
                else:
                    vertical += ' '
            i = len(vertical) - 1
            while vertical[i] == " ":
                i -= 1
            result.append(vertical[:i+1])
        return result
