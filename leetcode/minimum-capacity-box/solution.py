class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:

        new_list = [[capacity[i], i] for i in range(len(capacity))]
        new_list.sort()
        for i in range(len(new_list)):
            if new_list[i][0] >= itemSize:
                return new_list[i][1]
        return -1
