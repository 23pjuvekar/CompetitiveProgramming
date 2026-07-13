class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split();
        res = [];
        for word in words:
            if word[0] != '$' or word[1:].isnumeric() == False:
                res.append(word);
            else:
                price = int(word[1:]);
                #print(price);
                res.append("${:.2f}".format(price*(100 - discount)/100));

        return " ".join(res);
