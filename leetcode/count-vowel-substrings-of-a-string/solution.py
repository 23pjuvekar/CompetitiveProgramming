class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        vowels = 'aeiou'
        mp = defaultdict(int)
        for i, char in enumerate(word):
            if char in vowels:
                mp[char] += 1
                if i == 0 or word[i-1] not in vowels:
                    left = pivot = i
                while len(mp) == 5 and all(mp.values()):
                    mp[word[pivot]] -= 1
                    pivot += 1
                result += (pivot - left)
            else:
                mp.clear()
                left = pivot = i+1
        
        return result
