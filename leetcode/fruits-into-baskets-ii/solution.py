class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        unplaced = 0
        n = len(fruits)
        m = len(baskets)

        for i in range(n):
            placed = False
            for j in range(m):
                if baskets[j] >= fruits[i]:
                    baskets[j] = -1
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced
