class Solution:
    def arrangeWords(self, text: str) -> str:

        text = text.lower()
        arr = text.split(" ")
        c1 = defaultdict(list)
        mi = float("inf")
        ma = float("-inf")
        for word in arr:
            mi = min(mi, len(word))
            ma = max(ma, len(word))
            c1[len(word)].append(word)
        
        res = ""
        for i in range(mi, ma + 1):
            words = c1[i]
            for word in words:
                if res == "":
                    res = word[0].upper() + word[1:] + " "
                else:
                    res += word + " "
        return res[:len(res) - 1]
