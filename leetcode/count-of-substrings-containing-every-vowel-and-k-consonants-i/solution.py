class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def count_at_least(k_val):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            ans = 0
            left = 0
            consonants = 0
            vowel_map = defaultdict(int)
            
            for right in range(len(word)):
                if word[right] in vowels:
                    vowel_map[word[right]] += 1
                else:
                    consonants += 1
                
                while len(vowel_map) == 5 and consonants >= k_val:
                    ans += len(word) - right
                    
                    left_char = word[left]
                    if left_char in vowels:
                        vowel_map[left_char] -= 1
                        if vowel_map[left_char] == 0:
                            del vowel_map[left_char]
                    else:
                        consonants -= 1
                    left += 1
            return ans

        return count_at_least(k) - count_at_least(k + 1)
