class Solution:
    def minimumPushes(self, word: str) -> int:

        c = [val for key, val in Counter(word).items()]
        c.sort(reverse=True)
        print(c)
        total = 0
        for i in range(len(c)):
            total += c[i] * (i // 8 + 1)
        return total
