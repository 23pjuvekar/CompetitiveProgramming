class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        for key, val in Counter(suits).items():
            if val == 5:
                return "Flush"
        
        for key, val in dict(sorted(Counter(ranks).items(), reverse=True, key=lambda x: x[1])).items():
            print(key, val)
            if val > 2:
                return "Three of a Kind"
            elif val > 1:
                return "Pair"
        
        return "High Card"
