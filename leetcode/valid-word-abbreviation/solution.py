class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_len = len(word)
        abbr_len = len(abbr)
        word_p = 0
        abbr_p = 0

        while word_p < word_len and abbr_p < abbr_len:
            if abbr[abbr_p].isdigit():
                if abbr[abbr_p] == '0':
                    return False
                skip = 0
                while abbr_p < abbr_len and abbr[abbr_p].isdigit():
                    skip = skip * 10 + int(abbr[abbr_p])
                    abbr_p += 1

                if word_p + skip > word_len:
                    return False
                
                word_p += skip
            else:
                if word_p >= word_len or word[word_p] != abbr[abbr_p]:
                    return False
                word_p += 1
                abbr_p += 1

        
        return word_p == word_len and abbr_p == abbr_len
