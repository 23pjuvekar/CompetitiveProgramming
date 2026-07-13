class Solution:
    def minimumLength(self, s: str) -> int:

        counter = Counter(s)
        res = 0

        for letter, count in counter.items():
            while count >= 3:
                count -= 2
            res += count

        return res
