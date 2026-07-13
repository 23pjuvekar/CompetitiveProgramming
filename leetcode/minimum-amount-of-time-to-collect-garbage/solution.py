class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        letter_count = 0
        last_m = 0
        last_p = 0
        last_g = 0
        for i in range(len(garbage)):
            letter_count += len(garbage[i])
            if "M" in garbage[i]:
                last_m = i
            if "P" in garbage[i]:
                last_p = i
            if "G" in garbage[i]:
                last_g = i
        print(last_m, last_p, last_g)
        return letter_count + sum(travel[:last_m]) + sum(travel[:last_p]) + sum(travel[:last_g])
