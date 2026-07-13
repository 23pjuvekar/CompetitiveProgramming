class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        non_zero_indices = [0] * (n + 1)
        concatenation_prefix = [0] * (n + 1)
        digit_sum_prefix = [0] * (n + 1)
        powers_of_10 = [1] * (n + 1)

        for i in range(1, n + 1):
            powers_of_10[i] = (powers_of_10[i - 1] * 10) % MOD

        non_zero_count = 0
        for i, char in enumerate(s):
            digit = int(char)
            if digit != 0:
                non_zero_count += 1
                concatenation_prefix[non_zero_count] = (
                    concatenation_prefix[non_zero_count - 1] * 10 + digit
                ) % MOD
                digit_sum_prefix[non_zero_count] = (
                    digit_sum_prefix[non_zero_count - 1] + digit
                )
            
            non_zero_indices[i + 1] = non_zero_count

        results = []
        for left, right in queries:
            start_idx = non_zero_indices[left]
            end_idx = non_zero_indices[right + 1]

            if start_idx == end_idx:
                results.append(0)
                continue

            length = end_idx - start_idx
            segment_val = (
                concatenation_prefix[end_idx] - 
                concatenation_prefix[start_idx] * powers_of_10[length]
            ) % MOD
            
            segment_sum = digit_sum_prefix[end_idx] - digit_sum_prefix[start_idx]

            results.append((segment_val * segment_sum) % MOD)

        return results
