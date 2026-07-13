class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pair_set = set(nums)
        tracker = set()
        dup = Counter(nums)
        
        for p in pair_set:
            pos = p + k
            neg = p - k
            if pos in pair_set:
                if pos == p and dup[p] == 1:
                    continue
                if pos > p:
                    tracker.add((p, pos))
                else:
                    tracker.add((pos, p))
            elif neg in pair_set:
                if neg == p and dup[p] == 1:
                    continue
                if neg > p:
                    tracker.add((p, neg))
                else:
                    tracker.add((neg, p))
            
        print(tracker)
        return len(tracker)
