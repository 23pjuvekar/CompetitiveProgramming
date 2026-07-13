class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(list(s))
        list_heap = []
        for key, value in counter.items():
            list_heap.append([-value, key])

        heapq.heapify(list_heap)
        res = ""

        while list_heap:
            item = heapq.heappop(list_heap)
            if len(res) != 0 and item[1] == res[-1]:
                if len(list_heap) == 0:
                    return ""
                item_temp = heapq.heappop(list_heap)
                heapq.heappush(list_heap, item)
                item = item_temp
            res += item[1]
            item[0] += 1
            if item[0] != 0:
                heapq.heappush(list_heap, item)

        return res
