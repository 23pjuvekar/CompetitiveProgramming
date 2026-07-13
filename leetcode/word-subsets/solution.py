class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        word2_set = {}

        for word in words2:
            for item in Counter(word).items():
                word2_set[item[0]] = max(word2_set.get(item[0], 0), item[1])

        res = []
        for word in words1:
            word_count = Counter(word)
            good = True
            for item in word2_set.items():
                if word_count.get(item[0], 0) < item[1]:
                    good = False
                    break
            if good:
                res.append(word)
        
        return res
