class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:

        if len(capacity) < 3:
            return 0

        prefix = [0]
        for i in range(len(capacity)):
            prefix.append(capacity[i] + prefix[-1])

        res = 0
        counts = defaultdict(lambda: defaultdict(int))
        for r in range(len(capacity)):
            if r >= 2:
                l = r - 2
                counts[capacity[l]][prefix[l + 1] + capacity[l]] += 1
            res += counts[capacity[r]][prefix[r]]
        return res
            

        
        """
        map_id = defaultdict(list)
        prefix = [0]
        for i in range(len(capacity)):
            prefix.append(capacity[i] + prefix[-1])
            map_id[capacity[i]].append(i)
        res = 0
        for idx in map_id.values():
            for i_d in range(len(idx)):
                for j_d in range(i_d + 1, len(idx)):
                    i = idx[i_d]
                    j = idx[j_d]
                    total = (prefix[j+1] - prefix[i]) - capacity[i] - capacity[j]
                    if total == capacity[i] and total == capacity[j] and capacity[i] == capacity[j] and j - i + 1 >= 3:
                        res += 1
        return res
        """
