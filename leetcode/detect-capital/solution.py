class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        capital_amount = 0
        n = len(word)

        for i in range(n):
            if word[i] != word[i].lower():
                capital_amount += 1
        
        return (capital_amount == 1 and word[0] != word[0].lower()) or (capital_amount == n) or (capital_amount == 0)
