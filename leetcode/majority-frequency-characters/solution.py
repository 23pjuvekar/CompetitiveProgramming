class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        items = defaultdict(list)
        for key, val in Counter(s).items():
            items[val].append(key)
        
        res = []
        freq = -1
        for key, val in items.items():
            if len(res) < len(val):
                freq = key
                res = val
            elif len(res) == len(val) and freq < key:
                res = val
                freq = key
        return "".join(res)
