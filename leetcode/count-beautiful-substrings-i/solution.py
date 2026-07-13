class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:

        vowel_prefix = [0]
        consonant_prefix = [0]
        for c in s:
            if c in "aeiou":
                vowel_prefix.append(vowel_prefix[-1] + 1)
                consonant_prefix.append(consonant_prefix[-1])
            else:
                vowel_prefix.append(vowel_prefix[-1])
                consonant_prefix.append(consonant_prefix[-1] + 1)
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                vowels = vowel_prefix[j + 1] - vowel_prefix[i]
                consonants = consonant_prefix[j + 1] - consonant_prefix[i]
                if (vowels == consonants) and (vowels * consonants) % k == 0:
                    res += 1
        return res
