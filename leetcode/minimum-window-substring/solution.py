class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        target_counts = Counter(t)
        chars_needed_count = len(target_counts)
        window_counts = defaultdict(int)
        min_len = float('inf')
        min_start_index = 0
        l = 0
        for r in range(len(s)):
            char_r = s[r]
            window_counts[char_r] += 1
            if char_r in target_counts and window_counts[char_r] == target_counts[char_r]:
                chars_needed_count -= 1

            while chars_needed_count == 0:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    min_start_index = l

                char_l = s[l]
                window_counts[char_l] -= 1
                if char_l in target_counts and window_counts[char_l] < target_counts[char_l]:
                    chars_needed_count += 1
                
                l += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_start_index : min_start_index + min_len]
