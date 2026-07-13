class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(word):
            groups = []
            if not word: return groups
            curr_char = word[0]
            count = 0
            for char in word:
                if char == curr_char:
                    count += 1
                else:
                    groups.append((curr_char, count))
                    curr_char = char
                    count = 1
            groups.append((curr_char, count))
            return groups
        s_groups = get_groups(s)
        res = 0
        for word in words:
            w_groups = get_groups(word)
            if len(w_groups) != len(s_groups):
                continue
            is_stretchy = True
            for (char_w, count_w), (char_s, count_s) in zip(w_groups, s_groups):
                if char_w != char_s:
                    is_stretchy = False
                    break
                if count_w > count_s:
                    is_stretchy = False
                    break
                if count_w < count_s and count_s < 3:
                    is_stretchy = False
                    break
            
            if is_stretchy:
                res += 1
                
        return res
