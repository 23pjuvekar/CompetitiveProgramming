class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        curr = self.root

        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in curr.children:
                curr.children[(c1, c2)] = TrieNode()
            curr = curr.children[(c1, c2)]
            curr.count += 1
        
        return curr.count - 1

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        res = 0
        root = Trie()

        for w in reversed(words):
            res += root.add(w)
        
        return res
