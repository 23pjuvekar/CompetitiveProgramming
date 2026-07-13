class Solution:
    def sortVowels(self, s: str) -> str:

        count = defaultdict(int)
        first_occurrence = {}
        vowels = []

        for i in range(len(s)):
            if s[i] in "aeiou":
                count[s[i]] += 1
                if s[i] not in first_occurrence:
                    first_occurrence[s[i]] = i
                vowels.append(i)

        amts = sorted(count.items(), key=lambda x: (-x[1], first_occurrence[x[0]]))

        res = list(s)
        j = 0
        for i in vowels:
            while amts[j][1] == 0:
                j += 1
            res[i] = amts[j][0]
            amts[j] = (amts[j][0], amts[j][1] - 1)

        return "".join(res)
