class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = paragraph.replace(".", " ")
        paragraph =paragraph.replace(",", " ")
        paragraph =paragraph.replace("!", " ")
        paragraph =paragraph.replace("?", " ")
        paragraph =paragraph.replace("'", " ")
        paragraph =paragraph.replace(";", " ")
        arr = paragraph.lower().split(" ")
        print(arr)
        c1 = Counter(arr)
        res = ""
        count = 0
        banned.append("")
        for key, amt in c1.items():
            if key not in banned and amt > count:
                count = amt
                res = key
        return res
