class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n <= 1:
            return [0] * n
        
        def commonPrefixLength(s1, s2):
            length = 0
            min_len = min(len(s1), len(s2))
            for i in range(min_len):
                if s1[i] == s2[i]:
                    length += 1
                else:
                    break
            return length
        
        original_pairs = []
        for i in range(n - 1):
            original_pairs.append(commonPrefixLength(words[i], words[i + 1]))
        
        skip_pairs = {}
        for i in range(1, n - 1):
            skip_pairs[i] = commonPrefixLength(words[i - 1], words[i + 1])
        
        count = Counter(original_pairs)
        sorted_unique = sorted(count.keys(), reverse=True)
        
        result = []
        for skip in range(n):
            temp_count = count.copy()
            
            if skip < n - 1:
                temp_count[original_pairs[skip]] -= 1
                if temp_count[original_pairs[skip]] == 0:
                    del temp_count[original_pairs[skip]]
            
            if skip > 0:
                temp_count[original_pairs[skip - 1]] -= 1
                if temp_count[original_pairs[skip - 1]] == 0:
                    del temp_count[original_pairs[skip - 1]]
            
            if skip in skip_pairs:
                temp_count[skip_pairs[skip]] = temp_count.get(skip_pairs[skip], 0) + 1
            
            max_prefix = max(temp_count.keys()) if temp_count else 0
            result.append(max_prefix)
        
        return result
