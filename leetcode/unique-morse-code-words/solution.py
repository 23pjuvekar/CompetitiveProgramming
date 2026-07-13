class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        

        key = [
            ".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.",
            "---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
            ]

        res = set()

        for w in words:
            curr = ""
            for c in w:
                curr += key[ord(c) - ord("a")]
            res.add(curr)
        return len(res)
