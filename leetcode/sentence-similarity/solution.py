class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False
        pairs = defaultdict(set)
        for x, y in similarPairs:
            pairs[x].add(y)
            pairs[y].add(x)
        
        for w1, w2 in zip(sentence1, sentence2):
            if w2 not in pairs[w1] and w1 != w2:
                return False
        return True
