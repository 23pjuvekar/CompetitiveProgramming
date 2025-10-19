from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        n = len(s)
        b = b % n

        seen_list = set()
        curr_list = deque()
        curr_list.append(s)
        while curr_list:
            curr_string = curr_list.popleft()
            if curr_string in seen_list:
                continue
            seen_list.add(curr_string)
            new_string = ""
            for i in range(len(curr_string)):
                if i % 2 == 1:
                    new_string += str((int(curr_string[i]) + a) % 10)
                else:
                    new_string += curr_string[i]
            curr_list.append(new_string)
            new_string_2 = curr_string[n-b:] + curr_string[:n-b]
            curr_list.append(new_string_2)
        seen_list = list(seen_list)
        seen_list.sort()
        return seen_list[0]
        