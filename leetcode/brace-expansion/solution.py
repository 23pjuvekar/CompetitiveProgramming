class Solution:
    def expand(self, s: str) -> List[str]:

        options = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                i += 1
                group = []
                while s[i] != '}':
                    if s[i] != ',':
                        group.append(s[i])
                    i += 1
                group.sort()
                options.append(group)
            else:
                options.append([s[i]])
            i += 1
        
        results = []
        def backtrack(index, current_string):
            if index == len(options):
                results.append("".join(current_string))
                return
            for char in options[index]:
                current_string.append(char)
                backtrack(index + 1, current_string)
                current_string.pop()
                
        backtrack(0, [])
        return results
