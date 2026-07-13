class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)
        for start in range(len(s)):
            character = s[start]
            substring_length = 0
            for end in range(start, len(s)):
                if character == s[end]:
                    substring_length += 1
                    count[(character, substring_length)] += 1
                else:
                    break

        res = -1
        for key, amt in count.items():
            _, length = key
            if amt >= 3 and length > res:
                res = length
        return res
