class Solution:
    def smallestPalindrome(self, s: str) -> str:

        letters = list(set(s))
        letters.sort()
        count = Counter(s)
        end_value = ""
        word = ""
        for letter in letters:
            if count[letter] % 2 == 1:
                end_value = letter
                count[letter] -= 1
            for _ in range(count[letter] // 2):
                word += letter
        return word + end_value + word[::-1]

