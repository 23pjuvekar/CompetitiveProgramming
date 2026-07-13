class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:

        pizzas.sort(reverse=True)
        amount = len(pizzas) / 4
        even = int(amount // 2)
        odd = int(amount - even)
        res = 0
        print(pizzas)
        print(odd, even)

        i = -1
        while odd > 0:
            odd -= 1
            i += 1
            res += pizzas[i]
            

        while even > 0:
            i += 2
            even -= 1
            res += pizzas[i]
            
        return res
