class SegmentTree:
    def __init__(self, data):
        self.n = 2 ** math.ceil(math.log2(len(data)))
        self.tree = [0] * (2 * self.n)
        for i, val in enumerate(data):
            self.update(i + self.n, val)

    def update(self, index, value):
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])
                
    def find(self, data):
        if self.tree[1] < data:
            return -1
        index = 1
        while index < self.n:
            if self.tree[2 * index] >= data:
                index = 2 * index
            else:
                index = 2 * index + 1
        return index

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegmentTree(baskets)
        unplaced = 0
        for fruit in fruits:
            index = tree.find(fruit)
            if index == -1:
                unplaced += 1
            else:
                tree.update(index, -1)
        return unplaced
