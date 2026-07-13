class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        counter = Counter(s)
        res = []

        def bt(curr, counter):
            if len(curr) == len(s):
                res.append(curr)

            if not curr and len(s) % 2:
                for key in counter:
                    counter[key] -= 1
                    bt(key, counter)
                    counter[key] += 1
            else:
                for key, count in counter.items():
                    if count >= 2:
                        counter[key] -= 2
                        bt(key + curr + key, counter)
                        counter[key] += 2
    
        
        bt('', counter)
        return res
