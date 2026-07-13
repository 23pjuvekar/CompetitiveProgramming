class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        c1 = defaultdict(int)
        letters = set("abcdefghijklmnopqrstuvwxyz")

        for c in licensePlate:
            if c.lower() in letters:
                c1[c.lower()] += 1
        
        res = ""
        for word in words:
            c2 = Counter(word)
            good = True
            for key, val in c1.items():
                if c2[key] < c1[key]:
                    good = False
                    break
            if good:
                if res == "":
                    res = word
                elif len(res) > len(word):
                    res = word
        return res
