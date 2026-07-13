class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def score(word):
            count = defaultdict(int)
            min_word = word[0]
            for c in word:
                count[c] += 1
                min_word = min(min_word, c)
            return count[min_word]
        
        words_amount = defaultdict(int)
        for w in words:
            words_amount[score(w)] += 1
        answer = []
        for q in queries:
            amt = score(q)
            answer.append(0)
            for key, val in words_amount.items():
                if amt < key:
                    answer[-1] += val
        return answer
