class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1] * len(rains)
        dry_days = SortedList()
        full_lakes = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                dry_days.add(i)
            else:
                res[i] = -1
                if rain in full_lakes:
                    index_dry_possible = dry_days.bisect_right(full_lakes[rain])
                    if index_dry_possible == len(dry_days):
                        return []
                    res[dry_days[index_dry_possible]] = rain
                    dry_days.discard(dry_days[index_dry_possible])
                full_lakes[rain] = i
        return res
                    