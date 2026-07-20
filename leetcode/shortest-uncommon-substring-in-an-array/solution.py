class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        array_length = len(arr)
        result = []
        for current_index in range(array_length):
            current_string = arr[current_index]
            candidate_substrings = set()
            for start in range(len(current_string)):
                for end in range(start + 1, len(current_string) + 1):
                    candidate_substrings.add(current_string[start:end])

            sorted_candidates = sorted(candidate_substrings, key=lambda substring: (len(substring), substring))

            unique_substring = ""
            for candidate in sorted_candidates:
                found_elsewhere = False
                for other_index in range(array_length):
                    if other_index == current_index:
                        continue
                    if candidate in arr[other_index]:
                        found_elsewhere = True
                        break
                if found_elsewhere == False:
                    unique_substring = candidate
                    break

            result.append(unique_substring)
        return result
