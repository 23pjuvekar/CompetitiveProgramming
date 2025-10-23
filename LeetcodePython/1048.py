class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=lambda x: len(x))
        map_len = defaultdict(list)
        visited = set()

        for word in words:
            map_len[len(word)].append(word)
        
        res = 0

        for w in words:
            if w in visited:
                continue
            count = 0
            q = deque()
            q.append(w)
            while q:
                for _ in range(len(q)):
                    word = q.popleft()
                    if word in visited:
                        continue
                    visited.add(word)
                    for word2 in map_len[len(word) + 1]:
                        if self.good(word, word2):
                            q.append(word2)
                count += 1
                res = max(res, count)
        return res


    
    def good(self, word1, word2):
        skip = -1
        i = 0
        for w in word1:
            if w != word2[i]:
                if skip != -1:
                    return False
                elif word2[i + 1] != w:
                    return False
                else:
                    i += 1
                    skip = 1
            i += 1
        
        return len(word1) == len(word2) - 1


        