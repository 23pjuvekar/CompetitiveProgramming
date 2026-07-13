class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        s_chars = Counter(s)

        odd_count = 0
        total_items = 0
        for item in s_chars.items():
            if item[1] % 2 == 1:
                odd_count += 1
            total_items += item[1]

        return odd_count <= k and total_items >= k
