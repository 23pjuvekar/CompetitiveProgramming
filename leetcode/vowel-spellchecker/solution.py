class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        # Case 1
        reg_set = set(wordlist)

        # Case 2
        case_set = set()
        case_dict = {}
        for word in wordlist:
            lower_word = word.lower()
            case_set.add(lower_word)
            if lower_word not in case_dict:
                case_dict[lower_word] = word

        # Case 3
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        vowel_set = set()
        vowel_dict = {}
        for word in wordlist:
            word_lower = word.lower()
            word_final = ""
            for i in range(len(word_lower)):
                if word_lower[i] in vowels:
                    word_final += '*'
                else:
                    word_final += word_lower[i]
            vowel_set.add(word_final)
            if word_final not in vowel_dict:
                vowel_dict[word_final] = word


        res = []
        for q in queries:
            q_lower = q.lower()
            q_final = ""
            for i in range(len(q_lower)):
                if q_lower[i] in vowels:
                    q_final += '*'
                else:
                    q_final += q_lower[i]

            if q in reg_set:
                res.append(q)
            elif q_lower in case_set:
                res.append(case_dict[q_lower])
            elif q_final in vowel_set:
                res.append(vowel_dict[q_final])
            else:
                res.append("")

        return res
