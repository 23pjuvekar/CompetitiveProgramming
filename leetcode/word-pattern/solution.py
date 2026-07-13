class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        print(words)

        if len(pattern) != len(words):
            return False

        key = {}
        used_words = set()
        for i in range(len(words)):
            if pattern[i] not in key:
                if words[i] in used_words:
                    return False
                used_words.add(words[i])
                key[pattern[i]] = words[i]
            if key[pattern[i]] != words[i]:
                return False
        return True
