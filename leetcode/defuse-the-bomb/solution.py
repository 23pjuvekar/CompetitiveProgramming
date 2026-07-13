class Solution:
    def _calculate_positive_k_sum(self, arr: List[int], k_val: int) -> List[int]:
        n = len(arr)
        result_arr = [0] * n
        current_window_sum = 0
        for i in range(1, k_val + 1):
            current_window_sum += arr[i % n]
        result_arr[0] = current_window_sum
        for i in range(1, n):
            current_window_sum -= arr[i % n]
            current_window_sum += arr[(i + k_val) % n]
            result_arr[i] = current_window_sum
        return result_arr

    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        if k > 0:
            return self._calculate_positive_k_sum(code, k)
        else:
            abs_k = abs(k)
            reversed_code = code[::-1]
            temp_result = self._calculate_positive_k_sum(reversed_code, abs_k)
            return temp_result[::-1]
