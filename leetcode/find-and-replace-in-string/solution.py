class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        values = []
        for index, source, target in zip(indices, sources, targets):
            values.append((index, source, target))
        values.sort()
        i = 0
        j = 0
        res = []
        n = len(values)
        while i < len(s):
            found_match = False
            while j < n and values[j][0] == i:
                index, source, target = values[j]
                if s[i : i + len(source)] == source:
                    res.append(target)
                    i += len(source)
                    found_match = True
                    j += 1
                    break
                else:
                    j += 1
            
            if not found_match:
                res.append(s[i])
                i += 1
                
        return "".join(res)
