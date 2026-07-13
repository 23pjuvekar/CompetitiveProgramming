class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        counter = Counter(chars)
        res = 0

        for word in words:
            word_counter = Counter(word)
            good = True
            for key, value in word_counter.items():
                if key not in counter or counter[key] < value:
                    good = False
                    continue
            if good:
                res += len(word)
            
        return res
